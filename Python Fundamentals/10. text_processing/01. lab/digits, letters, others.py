string = input()
digits = []
letters = []
characters = []

for i in string:
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        letters.append(i)
    else:
        characters.append(i)

print(f"{''.join(digits)}\n"
      f"{''.join(letters)}\n"
      f"{''.join(characters)}")