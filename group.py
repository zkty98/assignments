import csv

with open('vegetable.csv','r') as f:
	reader= csv.DictReader(f)
	vegetables=list(reader)

from pprint import pprint 

vegetables_by_color = {}
for vegetable in vegetables:
	color = vegetable['color']
	if color in vegetables_by_color:
		vegetables_by_color[color].append(vegetable)
	else:
		vegetables_by_color[color] = [vegetable]


pprint(vegetables_by_color)
print(vegetables_by_color)

import json


with open('vegetables_by_color.json','w') as f:
	json.dump(vegetables_by_color,f,indent=2)