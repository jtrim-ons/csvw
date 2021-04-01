import csv
import json
import os
import sys

if len(sys.argv) < 2:
    sys.exit('Usage: {} FILENAME'.format(sys.argv[0]))

filepath = sys.argv[1]
_, filename = os.path.split(filepath)

with open(filepath, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(iter(csv_reader))

metadata = {
    "@context": "http://www.w3.org/ns/csvw",
    "url": "countries.csv",
    "tableSchema": {
        "columns": []
    }
}

for title in csv_header:
    metadata["tableSchema"]["columns"].append({
        "titles": title,
        "dc:description": "TODO"
    })

print(json.dumps(metadata, indent=2))

