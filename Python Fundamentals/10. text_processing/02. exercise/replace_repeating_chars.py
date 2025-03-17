string = input()
final_string = ""

for i in range(len(string)):
    if not final_string or string[i] != string[i - 1]:
        final_string += string[i]

print(final_string)