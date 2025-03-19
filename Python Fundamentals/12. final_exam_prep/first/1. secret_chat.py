message = input()

def insert_space(string, command):
    string = list(string)
    string.insert(int(command[1]), " ")
    return "".join(string)


def change_all(string, command):
    substring, replacement = command[1], command[2]
    if substring in string:
        string = string.replace(substring, replacement)
    return string


while True:
    command = input().split(":|:")

    if command[0] == "Reveal":
        break

    action = command[0]
    if action == "InsertSpace":
        message = insert_space(message, command)
        print(message)
    elif action == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")
    elif action == "ChangeAll":
        message = change_all(message, command)
        print(message)


print(f"You have a new text message: {message}")