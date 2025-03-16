import re

pattern_health = r'[^0-9\+\-\*\/\.]'
pattern_damage = r'[+-]?\d+\.?\d*'
demons_names = [demon.strip() for demon in input().split(",")]
demons = {}

for demon in demons_names:
    health = sum([ord(x) for x in re.findall(pattern_health, demon)])
    damage = sum([float(x) for x in re.findall(pattern_damage, demon)])
    for i in range(demon.count("*")):
        damage *= 2
    for i in range(demon.count("/")):
        damage /= 2

    demons[demon] = (health, damage)

for name, (health, damage) in dict(sorted(demons.items())).items():
    print(f"{name} - {health} health, {damage:.2f} damage")