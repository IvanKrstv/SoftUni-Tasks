import re

string = input()
word = input()

pattern = fr'\b{word}\b'

matches = re.findall(pattern, string, flags=re.I)
print(len(matches))