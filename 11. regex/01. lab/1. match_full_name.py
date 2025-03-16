import re

names = input()
pattern = r'\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b'
matches = re.findall(pattern, names)

if matches:
    print(" ".join(matches))