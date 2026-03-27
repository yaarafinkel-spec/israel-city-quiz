"""
Fetch Israeli cities and towns from OpenStreetMap via the Overpass API.
Saves a clean JSON file to data/cities.json.

OSM place tags used:
  - place=city  (~15 largest cities)
  - place=town  (mid-sized towns)
"""

import requests
import json

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

QUERY = """
[out:json][timeout:60];
area["name:en"="Israel"]["admin_level"="2"]->.searchArea;
(
  node["place"="city"](area.searchArea);
  node["place"="town"](area.searchArea);
);
out body;
"""

def fetch():
    print("Querying Overpass API...")
    response = requests.post(OVERPASS_URL, data={"data": QUERY}, timeout=90)
    response.raise_for_status()
    raw = response.json()

    cities = []
    for element in raw["elements"]:
        tags = element.get("tags", {})
        name_he = tags.get("name")           # Hebrew name (OSM default in Israel)
        name_en = tags.get("name:en")        # English name
        place   = tags.get("place")
        lat     = element.get("lat")
        lon     = element.get("lon")

        # Skip if missing essential fields
        if not name_he or not name_en or lat is None or lon is None:
            print(f"  Skipping (incomplete): {tags.get('name', '?')}")
            continue

        cities.append({
            "name_he": name_he,
            "name_en": name_en,
            "place":   place,
            "lat":     lat,
            "lon":     lon,
        })

    # Sort alphabetically by English name
    cities.sort(key=lambda c: c["name_en"])

    print(f"\nFetched {len(cities)} locations:")
    for c in cities:
        print(f"  [{c['place']:4s}] {c['name_en']} / {c['name_he']}  ({c['lat']:.4f}, {c['lon']:.4f})")

    out_path = "../data/cities.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(cities, f, ensure_ascii=False, indent=2)

    print(f"\nSaved to {out_path}")

if __name__ == "__main__":
    fetch()
