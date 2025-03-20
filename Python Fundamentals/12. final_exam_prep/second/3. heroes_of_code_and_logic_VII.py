n = int(input())
heroes = {}

def cast_spell(dic, com):
    name, mp_needed, spell = com[1], int(com[2]), com[3]
    if dic[name][1] >= mp_needed:
        dic[name][1] -= mp_needed
        print(f"{name} has successfully cast {spell} and now has {dic[name][1]} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell}!")
    return dic

def take_damage(dic, com):
    name, damage, attacker = com[1], int(com[2]), com[3]
    dic[name][0] -= damage
    if dic[name][0] <= 0:
        del dic[name]
        print(f"{name} has been killed by {attacker}!")
    else:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {dic[name][0]} HP left!")
    return dic

def recharge(dic, com):
    name, amount = com[1], int(com[2])
    current_mp = dic[name][1]
    dic[name][1] += amount
    if dic[name][1] > 200:
        dic[name][1] = 200
    print(f"{name} recharged for {dic[name][1] - current_mp} MP!")
    return dic

def heal(dic, com):
    name, amount = com[1], int(com[2])
    current_hp = dic[name][0]
    dic[name][0] += amount
    if dic[name][0] > 100:
        dic[name][0] = 100
    print(f"{name} healed for {dic[name][0] - current_hp} HP!")
    return dic


for i in range(n):
    name, hp, mp = input().split()
    hp, mp = int(hp), int(mp)
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200

    heroes[name] = [hp, mp]

while True:
    command = input().split(" - ")
    action = command[0]
    if action == "End":
        break

    if action == "CastSpell":
        heroes = cast_spell(heroes, command)
    elif action == "TakeDamage":
        heroes = take_damage(heroes, command)
    elif action == "Recharge":
        heroes = recharge(heroes, command)
    elif action == "Heal":
        heroes = heal(heroes, command)

for name, (hp, mp) in heroes.items():
    print(f"{name}\n  HP: {hp}\n  MP: {mp}")