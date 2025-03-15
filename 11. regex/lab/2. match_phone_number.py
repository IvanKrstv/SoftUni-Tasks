import re

string = input()
pattern = r'\+359([ -])2\1\d{3}\1\d{4}\b'

matches = re.finditer(pattern, string)

print(", ".join([match.group(0) for match in matches]))