string = input()
letters = set()
for letter in string:
    letters.add(letter)

for letter in sorted(letters):
    print(f'{letter}: {string.count(letter)} time/s')
