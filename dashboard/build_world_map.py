import json
import os
from shapely.geometry import Polygon

DASHBOARD_DIR = os.path.dirname(os.path.abspath(__file__))
TOPO_FILE = os.path.join(DASHBOARD_DIR, "world-countries-110m.json")
OUTPUT_FILE = os.path.join(DASHBOARD_DIR, "world_path.txt")

# source: https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json (Natural Earth 110m, public domain)
topo = json.load(open(TOPO_FILE))
scale_x, scale_y = topo["transform"]["scale"]
trans_x, trans_y = topo["transform"]["translate"]


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
        return decode_arc(topo["arcs"][arc_index])
    else:
        real_index = ~arc_index
        return list(reversed(decode_arc(topo["arcs"][real_index])))


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
geoms = topo["objects"]["countries"]["geometries"]
total_rings = 0
kept_rings = 0

for geom in geoms:
    if geom["properties"]["name"] == "Antarctica":
        continue
    gtype = geom["type"]
    arcs = geom["arcs"]
    if gtype == "Polygon":
        polys = [arcs]
    elif gtype == "MultiPolygon":
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

        # A ring whose raw longitudes span most of the globe (e.g. Russia,
        # whose Chukotka peninsula dips just past -180 while the rest of the
        # country sits at positive longitudes) doesn't actually span the
        # globe - it crosses the antimeridian. Left as-is, Polygon()/simplify()
        # would connect a point near +180 straight to one near -180 in raw
        # coordinate space, corrupting the shape with a spurious ~360deg-wide
        # edge. Unwrap first (extend eastward past +180 instead of wrapping
        # to -180) so simplification operates on a topologically sane ring,
        # then split back into left/right-of-seam pieces at emit time.
        def unwrap_ring(ring):
            if not ring:
                return ring
            out = [ring[0]]
            for prev, cur in zip(ring, ring[1:]):
                lon, lat = cur
                while lon - out[-1][0] > 180:
                    lon -= 360
                while lon - out[-1][0] < -180:
                    lon += 360
                out.append((lon, lat))
            return out

        all_lons = [c[0] for c in exterior]
        crosses_seam = max(all_lons) - min(all_lons) > 180
        if crosses_seam:
            exterior = unwrap_ring(exterior)
            holes = [unwrap_ring(h) for h in holes]

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
            is_closed_ring = coords[0] == coords[-1]

            # coords may now be unwrapped (lon outside [-180, 180]) if this
            # ring crossed the seam. Cut it back into map-space fragments at
            # each +/-180 crossing, inserting the interpolated seam point on
            # both sides, and re-wrap each fragment's longitudes into
            # [-180, 180] for projection.
            fragments = [[coords[0]]]
            for prev, cur in zip(coords, coords[1:]):
                # In unwrapped space, "which copy of the seam" a point falls
                # after is floor((lon+180)/360). A ring segment crosses a
                # +/-180 meridian whenever consecutive points land in
                # different copies.
                seam_n_prev = (prev[0] + 180) // 360
                seam_n_cur = (cur[0] + 180) // 360
                if seam_n_prev != seam_n_cur:
                    seam_lon = (
                        max(seam_n_prev, seam_n_cur) * 360 - 180
                        if cur[0] > prev[0]
                        else min(seam_n_prev, seam_n_cur) * 360 + 180
                    )
                    t = (
                        (seam_lon - prev[0]) / (cur[0] - prev[0])
                        if cur[0] != prev[0]
                        else 0.5
                    )
                    lat_at_seam = prev[1] + t * (cur[1] - prev[1])
                    fragments[-1].append((seam_lon, lat_at_seam))
                    fragments.append([(seam_lon, lat_at_seam)])
                fragments[-1].append(cur)

            if is_closed_ring and len(fragments) > 1:
                # The ring's start point is arbitrary, so the first and last
                # fragments are actually one continuous physical piece
                # (connected through the wrap-around) - stitch them.
                first = fragments.pop(0)
                fragments[-1].extend(first[1:])

            def rewrap(lon):
                while lon > 180:
                    lon -= 360
                while lon < -180:
                    lon += 360
                return lon

            for frag in fragments:
                if len(frag) < 2:
                    continue
                frag = [(rewrap(lon), lat) for lon, lat in frag]
                on_seam = abs(frag[0][0]) == 180 and abs(frag[-1][0]) == 180
                if on_seam and frag[0] != frag[-1] and frag[0][0] == frag[-1][0]:
                    # Both ends sit on the same seam meridian at different
                    # latitudes - close the polygon by running along that
                    # meridian back to the start, or the fill renders torn.
                    frag = frag + [frag[0]]
                kept_rings += 1
                pts = [project(lon, lat) for lon, lat in frag]
                d = f"M{pts[0][0]:.0f},{pts[0][1]:.0f} " + " ".join(
                    f"L{x:.0f},{y:.0f}" for x, y in pts[1:]
                )
                if frag[0] == frag[-1]:
                    d += " Z"
                path_parts.append(d)

        geoms_to_emit = []
        if simplified.geom_type == "Polygon":
            geoms_to_emit = [simplified]
        elif simplified.geom_type == "MultiPolygon":
            geoms_to_emit = list(simplified.geoms)

        for g in geoms_to_emit:
            if g.exterior:
                emit_ring(list(g.exterior.coords))
            for interior in g.interiors:
                emit_ring(list(interior.coords))

full_path = " ".join(path_parts)
print(f"Rings: {total_rings} -> kept {kept_rings}")
print(f"Path length: {len(full_path)} chars")

with open(OUTPUT_FILE, "w") as f:
    f.write(full_path)
