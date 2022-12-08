import json
import csv

import html2text

json_file = "input/cab_search.json"
csv_file = "output/cab_data.csv"

with open(json_file, "r") as f:
    data = json.load(f)

results = data["results"]["results"]

with open(csv_file, "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)

    count = 0

    for result in results:
        # Header stuff
        if count == 0:
            header = result.keys()
            csv_writer.writerow(header)
            count += 1
        
        # Remove HTML tags
        if "title" in result:
            result["title"] = html2text.html2text(result["title"]).strip()
        if "description" in result:
            result["description"] = \
                html2text.html2text(result["description"]).strip()
        if "htmlcontent" in result:
            result["htmlcontent"] = \
                html2text.html2text(result["htmlcontent"]).strip()

        # Do stuff with lists
        if len(result["tags"]) >= 1:
            temp = ", ".join(filter(
                lambda x: x if x is not None else '', result["tags"]
            ))
            if temp == "[]" or temp == []: b == ""
            result["tags"] = temp
        if len(result["regions"]) >= 1:
            temp = ", ".join(filter(
                lambda x: x if x is not None else '', result["regions"]
            ))
            if temp == "[]" or temp == []: b == ""
            result["regions"] = temp
        if len(result["cities"]) >= 1:
            temp = ", ".join(filter(
                lambda x: x if x is not None else '', result["cities"]
            ))
            if temp == "[]" or temp == []: temp == ""
            result["cities"] = temp
        
        # Location stuff
        if "location" in result and result["location"] != None:
            location = result["location"]
            result["location"] = f"Latitude: {location['lat']}\n\
Longitude: {location['lng']}"
        elif "location" in result and result["location"] == None:
            result["location"] == ""

        csv_writer.writerow(result.values())
