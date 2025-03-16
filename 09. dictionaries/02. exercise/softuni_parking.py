user_cars = {}

def register(my_dict: dict, com: list):
    username, license_plate = com[1], com[2]
    if username in my_dict.keys():
        print(f"ERROR: already registered with plate number {my_dict[username]}")
    else:
        my_dict[username] = license_plate
        print(f"{username} registered {license_plate} successfully")
    return my_dict

def unregister(my_dict: dict, com: list):
    username = com[1]
    if username not in my_dict.keys():
        print(f"ERROR: user {username} not found")
    else:
        del my_dict[username]
        print(f"{username} unregistered successfully")
    return my_dict

n = int(input())
for i in range(n):
    command = input().split()
    action = command[0]

    if action == "register":
        user_cars = register(user_cars, command)
    elif action == "unregister":
        user_cars = unregister(user_cars, command)

for key, value in user_cars.items():
    print(f"{key} => {value}")