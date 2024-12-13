import json

# Open and load the JSON file
with open('./PokeTCG.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)
#print the name of all fighting type pokemon

#print all cards from the set "HeartGold & SoulSilver"

#print all cards where the averageSellPrice is greater than 1.5

""" print(data) """

for pokemon in data:
    if data['data'] == data{'type'["fighting"]}:
        print(pokemon['name'])
        found = True
    else:
        print("Pokemon not found")

""" for pokemon in data:
    if pokemon["series"] == pokemon["HeartGold & SoulSilver"]:
        print(pokemon["name"])
    found = True
    if not found:
        print("Pokemon not found") """

""" averageSellPrice = pokemon['averageSellPrice']

for pokemon in data:
    if averageSellPrice > float(1.5):
        print(pokemon["name"])
    found = True
    if not found:
        print("Pokemon not found") """

