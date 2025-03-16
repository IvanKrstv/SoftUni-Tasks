string = input()
letters = {}

for letter in string:
    if letter == " ":
        continue

    if letter not in letters:
        letters[letter] = 0
    letters[letter] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")