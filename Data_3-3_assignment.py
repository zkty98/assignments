# load libaray
import json

#read superheroes.json
with open ('superheroes.json','r') as f:
	superheroes = json.load(f)

members=superheroes['members']

import csv

with open('superheroes.csv','w') as f:
	writer= csv.writer(f)
	writer.writerow(['name',"age",'secretIdentity','powers','squadName','homeTown','formed','secretBase','active'])
	

	for member in members:
		name= member['name']
		age= member['age']
		secretIdentity = member['secretIdentity']
		powers = member['powers']

		squadName= superheroes['squadName']
		homeTown=superheroes['homeTown']
		formed=superheroes['formed']
		secretBase=superheroes['secretBase']
		active=superheroes['active']



		row=[name,age, secretIdentity,powers,squadName,homeTown,formed,secretBase,active]
		
		writer.writerow(row)