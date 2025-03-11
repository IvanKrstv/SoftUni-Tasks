n = int(input())
dragons = {}
for i in range(n):
    type, name, damage, health, armor = input().split()
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    damage, health, armor = int(damage), int(health), int(armor)

