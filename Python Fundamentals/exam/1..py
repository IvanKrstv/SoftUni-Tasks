string = input()

def translate(word, com):
    char, replacement = com[1], com[2]
    print(word.replace(char, replacement))
    return word.replace(char, replacement)

def includes(word, com):
    substring = com[1]
    if substring in word:
        return True
    return False

def start(word: str, com):
    substring = com[1]
    if word.startswith(substring):
        return True
    return False

def lowercase(word: str):
    print(word.lower())
    return word.lower()

def find_index(word: str, com):
    char = com[1]
    print(word.rindex(char))

def remove(word: str, com):
    start_index, count = int(com[1]), int(com[2])
    new_string = word[:start_index] + word[start_index + count:]
    print(new_string)
    return new_string

while True:
    command = input().split()
    action = command[0]
    if action == "End":
        break

    if action == "Translate":
        string = translate(string, command)
    elif action == "Includes":
        print(includes(string, command))
    elif action == "Start":
        print(start(string, command))
    elif action == "Lowercase":
        string = lowercase(string)
    elif action == "FindIndex":
        find_index(string, command)
    elif action == "Remove":
        string = remove(string, command)
