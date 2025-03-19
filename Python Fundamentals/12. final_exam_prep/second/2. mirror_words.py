import re

string = input()
pattern = r'([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})'
mirror_words = []
matches = re.findall(pattern, string)

if not matches:
    print("No word pairs found!")
else:
    for match in matches:
        first_word, second_word = match[1], match[2]
        if first_word == second_word[::-1]:
            mirror_words.append(f"{first_word} <=> {second_word}")
    print(f"{len(matches)} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print(f"The mirror words are:\n{', '.join(mirror_words)}")