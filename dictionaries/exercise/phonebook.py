phonebook = {}

while True:
    info = input().split("-")

    if info[0].isdigit():
        n = int(info[0])
        break

    name, number = info[0], info[1]

    phonebook[name] = number

for i in range(n):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")