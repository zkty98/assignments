import csv
import json

with open('vegetable.csv','r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)


with open ('vegetable.json','w') as f:
	json.dump(rows, f, indent=2)
