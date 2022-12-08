import json
import csv

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
        
        csv_writer.writerow(result.values())
