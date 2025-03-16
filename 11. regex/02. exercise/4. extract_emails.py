import re

string = input()
pattern = r'\s([a-z0-9])+[a-z0-9\.\-\_]*@([a-z\-]+)(\.[a-z]+)+\b'

matches = re.finditer(pattern, string)

for match in matches:
    print(match.group())
