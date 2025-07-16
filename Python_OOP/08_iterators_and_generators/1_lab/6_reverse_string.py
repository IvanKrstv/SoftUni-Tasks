def reverse_text(string: str):
    # index = 0
    # while index < len(string):
    #     yield string[::-1][index]
    #     index += 1

    index = len(string) - 1
    while index >= 0:
        yield string[index]
        index -= 1

for char in reverse_text("step"):
    print(char, end='')
