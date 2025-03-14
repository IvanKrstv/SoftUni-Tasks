text = input()
new_text = ""
for character in text:
    new_text += chr(ord(character) + 3)

print(new_text)