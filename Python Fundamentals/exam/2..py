import re

n = int(input())
pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

for i in range(n):
    string = input()
    if not re.search(pattern, string):
        print("The message is invalid")
        continue

    command, valid_string = re.search(pattern, string).groups()
    result = f"{command}:"
    for char in valid_string:
        result += " " + str(ord(char))

    print(result.rstrip())