import re

pattern = r'@([A-Za-z]+)[^@\-!\:\>]*:(\d+)[^@\-!\:\>]*!(A|D)![^@\-!\:\>]*->(\d+)'
n = int(input())
attacked_planets = []
destroyed_planets = []

for i in range(n):
    message = input()
    count_letters = message.lower().count('s') + message.lower().count('t') + message.lower().count('a') + message.lower().count('r')

    decrypted_message = ""
    for letter in message:
        decrypted_message += chr(ord(letter) - count_letters)

    match = re.search(pattern, decrypted_message)
    if match:
        name, population, attack_type, soldier_count = match.groups()
        if attack_type == "A":
            attacked_planets.append(name)
        else:
            destroyed_planets.append(name)

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")