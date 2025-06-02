import re

with open('words.txt') as f:
    words = {word: 0 for word in f.read().split()}

with open('input.txt') as f:
    text = f.read()

for word in words:
    regex = rf'\b{word}\b'
    matches = re.findall(regex, text, re.IGNORECASE)
    words[word] = len(matches)

for key, value in sorted(words.items(), key=lambda x: -x[1]):
    print(f'{key} - {value}')