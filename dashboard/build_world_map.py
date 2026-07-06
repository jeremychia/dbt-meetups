import json, os
from shapely.geometry import Polygon

DASHBOARD_DIR = os.path.dirname(os.path.abspath(__file__))
TOPO_FILE = os.path.join(DASHBOARD_DIR, 'world-countries-110m.json')
OUTPUT_FILE = os.path.join(DASHBOARD_DIR, 'world_path.txt')

# source: https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json (Natural Earth 110m, public domain)
topo = json.load(open(TOPO_FILE))
scale_x, scale_y = topo['transform']['scale']
trans_x, trans_y = topo['transform']['translate']

def decode_arc(arc):
    coords = []
    x, y = 0, 0
    for dx, dy in arc:
        x += dx
        y += dy
        lon = x * scale_x + trans_x
        lat = y * scale_y + trans_y
        coords.append((lon, lat))
    return coords

def get_arc_coords(arc_index):
    if arc_index >= 0:
        return decode_arc(topo['arcs'][arc_index])
    else:
        real_index = ~arc_index
        return list(reversed(decode_arc(topo['arcs'][real_index])))

def ring_from_arcs(arc_list):
    coords = []
    for arc_index in arc_list:
        pts = get_arc_coords(arc_index)
        if coords and coords[-1] == pts[0]:
            coords.extend(pts[1:])
        else:
            coords.extend(pts)
    return coords

VIEWBOX_W = 960
VIEWBOX_H = 500

def project(lon, lat):
    x = (lon + 180) / 360 * VIEWBOX_W
    y = (90 - lat) / 180 * VIEWBOX_H
    return x, y

SIMPLIFY_TOLERANCE_DEG = 0.4  # degrees, in lon/lat space before projection

path_parts = []
geoms = topo['objects']['countries']['geometries']
total_rings = 0
kept_rings = 0

for geom in geoms:
    if geom['properties']['name'] == 'Antarctica':
        continue
    gtype = geom['type']
    arcs = geom['arcs']
    if gtype == 'Polygon':
        polys = [arcs]
    elif gtype == 'MultiPolygon':
        polys = arcs
    else:
        continue
    for poly in polys:
        exterior = None
        holes = []
        for i, ring_arcs in enumerate(poly):
            ring = ring_from_arcs(ring_arcs)
            total_rings += 1
            if len(ring) < 3:
                continue
            if i == 0:
                exterior = ring
            else:
                holes.append(ring)
        if not exterior:
            continue
        try:
            shp = Polygon(exterior, holes)
            if not shp.is_valid:
                shp = shp.buffer(0)
            simplified = shp.simplify(SIMPLIFY_TOLERANCE_DEG, preserve_topology=True)
        except Exception:
            continue

        def emit_ring(coords):
            global kept_rings
            if len(coords) < 3:
                return
            # Split at antimeridian crossings (lon jump > 180deg between consecutive
            # points), inserting an interpolated point exactly at +/-180 so each
            # side of a real landmass (e.g. Russia, which spans ~170deg of
            # longitude) is cut precisely at the seam rather than discarded by a
            # blunt "span > 90deg" heuristic, which drops genuine wide landmasses
            # along with true degenerate slivers.
            segments = [[coords[0]]]
            for prev, cur in zip(coords, coords[1:]):
                if abs(cur[0] - prev[0]) > 180:
                    # interpolate the crossing point at the seam on both sides
                    edge = 180 if prev[0] > 0 else -180
                    other_edge = -edge
                    # linear interpolation in unwrapped space
                    prev_unwrapped = prev[0]
                    cur_unwrapped = cur[0] + (360 if cur[0] < 0 else -360)
                    t = (edge - prev_unwrapped) / (cur_unwrapped - prev_unwrapped) if cur_unwrapped != prev_unwrapped else 0.5
                    lat_at_seam = prev[1] + t * (cur[1] - prev[1])
                    segments[-1].append((edge, lat_at_seam))
                    segments.append([(other_edge, lat_at_seam)])
                segments[-1].append(cur)
            for seg in segments:
                if len(seg) < 2:
                    continue
                kept_rings += 1
                pts = [project(lon, lat) for lon, lat in seg]
                d = f"M{pts[0][0]:.0f},{pts[0][1]:.0f} " + " ".join(f"L{x:.0f},{y:.0f}" for x, y in pts[1:])
                if len(seg) > 2 and seg[0] == coords[0] and seg[-1] == coords[-1]:
                    d += " Z"
                path_parts.append(d)

        geoms_to_emit = []
        if simplified.geom_type == 'Polygon':
            geoms_to_emit = [simplified]
        elif simplified.geom_type == 'MultiPolygon':
            geoms_to_emit = list(simplified.geoms)

        for g in geoms_to_emit:
            if g.exterior:
                emit_ring(list(g.exterior.coords))
            for interior in g.interiors:
                emit_ring(list(interior.coords))

full_path = " ".join(path_parts)
print(f"Rings: {total_rings} -> kept {kept_rings}")
print(f"Path length: {len(full_path)} chars")

with open(OUTPUT_FILE, 'w') as f:
    f.write(full_path)
