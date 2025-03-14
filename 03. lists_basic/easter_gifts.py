gifts = input().split()

command = input()
while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for index in range(len(gifts)):
            if command[1] == gifts[index]:
                gifts[index] = "None"
    elif "Required" in command:
        for index in range(len(gifts)):
            if index == int(command[2]) and int(command[2]) < len(gifts):
                gifts[index] = command[1]
                break
    elif "JustInCase" in command:
        gifts[-1] = command[1]
    command = input()

final_list = []
for element in gifts:
    if element != "None":
        final_list.append(element)
print(" ".join(final_list))