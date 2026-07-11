# Country -> broad region, with the Americas/Europe split further by sub-region
# as requested for chapter filtering.
COUNTRY_REGION = {
    "USA": "North America",
    "Canada": "North America",
    "Mexico": "North America",
    "Colombia": "Latin America",
    "Argentina": "Latin America",
    "Brazil": "Latin America",
    "UK": "Northern Europe",
    "Ireland": "Northern Europe",
    "Netherlands": "Western Europe",
    "Belgium": "Western Europe",
    "France": "Western Europe",
    "Germany": "Western Europe",
    "Switzerland": "Western Europe",
    "Austria": "Western Europe",
    "Denmark": "Northern Europe",
    "Norway": "Northern Europe",
    "Sweden": "Northern Europe",
    "Finland": "Northern Europe",
    "Lithuania": "Northern Europe",
    "Spain": "Southern Europe",
    "Italy": "Southern Europe",
    "Greece": "Southern Europe",
    "Czechia": "Central & Eastern Europe",
    "Slovakia": "Central & Eastern Europe",
    "Hungary": "Central & Eastern Europe",
    "Romania": "Central & Eastern Europe",
    "Nigeria": "Africa",
    "India": "Asia",
    "China": "Asia",
    "Vietnam": "Asia",
    "Philippines": "Asia",
    "Singapore": "Asia",
    "Taiwan": "Asia",
    "South Korea": "Asia",
    "Japan": "Asia",
    "Australia": "Oceania",
    "New Zealand": "Oceania",
    "UAE": "Middle East",
    "Saudi Arabia": "Middle East",
    "Israel": "Middle East",
}

REGION_GROUP = {
    "North America": "Americas",
    "Latin America": "Americas",
    "Northern Europe": "Europe",
    "Western Europe": "Europe",
    "Southern Europe": "Europe",
    "Central & Eastern Europe": "Europe",
    "Africa": "Africa",
    "Asia": "Asia",
    "Oceania": "Oceania",
    "Middle East": "Middle East",
}


def region_for(country):
    sub = COUNTRY_REGION.get(country)
    group = REGION_GROUP.get(sub)
    return {"sub_region": sub, "region_group": group}
