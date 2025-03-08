def position(letter):
    pos = ord(letter.upper()) - 64
    return pos

def first_letter(word: str):
    letter = word[0]
    number = int(word[1:-1])
    pos = position(letter)
    if letter.isupper():
        result = number / pos
    else:
        result = number * pos
    return result

def last_letter(word: str):
    letter = word[-1]
    number = first_letter(word)
    pos = position(letter)
    if letter.isupper():
        result = number - pos
    else:
        result = number + pos
    return result

string = input().split()
total_sum = 0
for element in string:
    total_sum += last_letter(element)

print(f"{total_sum:.2f}")