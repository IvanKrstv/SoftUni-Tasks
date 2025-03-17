force = {}

def first_option(my_dict: dict, com: list):
    force_side, force_user = com[0], com[1]

    if force_side not in my_dict.keys():
        my_dict[force_side] = []
    for lst in my_dict.values():
        if force_user in lst:
            return my_dict
    my_dict[force_side].append(force_user)

    return my_dict

def second_option(my_dict: dict, com: list):
    force_user, force_side = com[0], com[1]

    if force_side not in my_dict.keys():
        my_dict[force_side] = []
    for lst in my_dict.values():
        if force_user in lst:
            lst.remove(force_user)
            break

    my_dict[force_side].append(force_user)
    print(f"{force_user} joins the {force_side} side!")

    return my_dict

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        force = first_option(force, command.split(" | "))

    elif "->" in command:
        force = second_option(force, command.split(" -> "))

for side, users in force.items():
    if not users:
        continue

    print(f"Side: {side}, Members: {len(users)}")
    print(f"!", '\n! '.join(users))
