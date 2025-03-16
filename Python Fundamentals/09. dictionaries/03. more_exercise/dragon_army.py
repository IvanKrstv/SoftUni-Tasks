dragon_types = {}
dragon_names = {}

def average(attribute, given_type):
    suma = sum([dragon_names[tip, ime][attribute] for (tip, ime) in dragon_names.keys() if tip == given_type])
    length = len([dragon_names[tip, ime][attribute] for (tip, ime) in dragon_names.keys() if tip == given_type])
    return suma / length

n = int(input())
for i in range(n):
    type, name, damage, health, armor = input().split()
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    damage, health, armor = int(damage), int(health), int(armor)

    if type not in dragon_types:
        dragon_types[type] = []
    if name not in dragon_types[type]:
        dragon_types[type].append(name)

    if (type, name) not in dragon_names:
        dragon_names[(type, name)] = {}
    dragon_names[(type, name)]['damage'] = damage
    dragon_names[(type, name)]['health'] = health
    dragon_names[(type, name)]['armor'] = armor

for type, names in dragon_types.items():
    print(f"{type}::({average('damage', type):.2f}/{average('health', type):.2f}/{average('armor', type):.2f})")
    for name in sorted(names):
        print(f"-{name} -> damage: {dragon_names[(type, name)]['damage']}, health: {dragon_names[(type, name)]['health']}, armor: {dragon_names[(type, name)]['armor']}")