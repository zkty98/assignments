import csv

with open('vegetable.csv','r') as f:
	reader= csv.DictReader(f)
	vegetables=list(reader)


green_vegetables = []

whitelist = ['green']
for vegetable in vegetables:
	if vegetable['color'] in whitelist:
		green_vegetables.append(vegetable)

print (green_vegetables)


with open ('green_vegetables.csv','w') as f:
	writer = csv.writer(f)