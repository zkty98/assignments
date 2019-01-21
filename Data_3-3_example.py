# load libaray
import json

#read superheroes.json
with open ('superheroes.json','r') as f:
	superheroes = json.load(f)

members = superheroes['members']

print(members)

#loop through each member

for member in members:
	#for each member get a list of powers 
	powers= member['powers']
	print(powers)

	#loop through the powers and print each one 
	for power in powers:
		print(power)

		unique_power = list (set (powers))
		print (unique_power)