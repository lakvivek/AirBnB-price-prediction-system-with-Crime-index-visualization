import csv
import json
import os

csvfile = "../data/processed_NYPD"

jsonfile = csvfile + '.json'

with open(csvfile+'.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open(jsonfile, 'w') as f:
    json.dump(rows, f)
