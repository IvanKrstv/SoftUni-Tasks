targets = [int(num) for num in input().split()]

def shoot(lst: list, com: list) -> list:
    index, power = int(com[1]), int(com[2])
    if 0 <= index < len(lst):
        lst[index] -= power
        if lst[index] <= 0:
            lst.pop(index)
    return lst

def add(lst: list, com: list) -> list:
    index, value = int(com[1]), int(com[2])
    if 0 <= index < len(lst):
        lst.insert(index, value)
    else:
        print("Invalid placement!")

    return lst

def strike(lst: list, com: list) -> list:
    index, radius = int(com[1]), int(com[2])
    if 0 <= index - radius and index + radius < len(lst):
        first_part = lst[:index - radius]
        second_part = lst[index + radius + 1:]
        return first_part + second_part
    else:
        print("Strike missed!")
    return lst

command = input().split()

while command[0] != "End":
    action = command[0]

    if action == "Shoot":
        targets = shoot(targets, command)
    elif action == "Add":
        targets = add(targets, command)
    elif action == "Strike":
        targets = strike(targets, command)

    command = input().split()


print("|".join(list(map(str,targets))))