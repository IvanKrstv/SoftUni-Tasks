my_dict = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in my_dict:
        my_dict[resource] = quantity
    else:
        my_dict[resource] += quantity

for key, value in my_dict.items():
    print(f"{key} -> {value}")