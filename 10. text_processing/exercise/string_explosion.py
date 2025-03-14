string = input()
strength = 0
final_string = ""
for i in range(len(string)):
    if strength == 0 and string[i] != ">":
        final_string += string[i]

    elif string[i] == ">":
        strength += int(string[i + 1])
        final_string += ">"

    elif strength != 0:
        strength -= 1

print(final_string)