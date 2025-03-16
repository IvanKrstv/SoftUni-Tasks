import re

string = input()
pattern = r'(^|(?<=\s))-?(0|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

numbers = re.finditer(pattern, string)

for number in numbers:
    print(number.group(), end=" ")
