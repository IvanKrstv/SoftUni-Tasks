import re

string = input()
pattern = r'www\.([a-zA-Z0-9\-]+)(\.[a-z]+)+'

while string:
    matches = re.search(pattern, string)
    if matches:
        print(matches.group())

    string = input()