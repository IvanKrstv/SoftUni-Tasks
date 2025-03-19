n = int(input())
dict = {}


def add(my_dict, comm):
    piece, composer, key = comm[1], comm[2], comm[3]
    if piece not in my_dict.keys():
        my_dict[piece] = (composer, key)
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")

    return my_dict


def remove_(my_dict: dict, com):
    piece = com[1]
    if piece in my_dict.keys():
        my_dict.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return my_dict


def change_key(my_dict, com):
    piece, new_key = com[1], com[2]
    if piece in my_dict:
        composer = my_dict[piece][0]
        my_dict[piece] = (composer, new_key)
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return my_dict

for i in range(n):
    piece, composer, key = input().split("|")
    dict[piece] = (composer, key)

while True:
    command = input().split("|")
    action = command[0]

    if action == "Stop":
        break

    if action == "Add":
        dict = add(dict, command)
    elif action == "Remove":
        dict = remove_(dict, command)
    elif action == "ChangeKey":
        dict = change_key(dict, command)

for piece, (composer, key) in dict.items():
    print(f"{piece} -> Composer: {composer}, Key: {key}")
