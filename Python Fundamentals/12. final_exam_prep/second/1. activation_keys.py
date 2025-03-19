activation_key = input()


def contains(key, com):
    substring = com[1]
    if substring in key:
        return f"{key} contains {substring}"
    else:
        return "Substring not found!"


def flip(key, com):
    start_index, end_index = int(com[2]), int(com[3])
    if com[1] == "Lower":
        key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
    elif com[1] == "Upper":
        key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
    return key


def slice(key, com):
    start_index, end_index = int(com[1]), int(com[2])
    key = key[:start_index] + key[end_index:]
    return key


while True:
    command = input().split(">>>")
    action = command[0]
    if action == "Generate":
        break

    if action == "Contains":
        print(contains(activation_key, command))
    elif action == "Flip":
        activation_key = flip(activation_key, command)
        print(activation_key)
    elif action == "Slice":
        activation_key = slice(activation_key, command)
        print(activation_key)

print(f"Your activation key is: {activation_key}")