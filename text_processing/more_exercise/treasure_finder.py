key = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "find":
        break
    encrypted_message = ""
    current_list_index = 0
    for char in command:
        encrypted_message += chr(ord(char) - key[current_list_index])
        current_list_index += 1
        if current_list_index == len(key):
            current_list_index = 0

    first_index = encrypted_message.index("&")
    second_index = encrypted_message.rindex("&")
    index_left = encrypted_message.index("<")
    index_right = encrypted_message. index(">")

    type = encrypted_message[first_index + 1:second_index]
    coordinates = encrypted_message[index_left + 1:index_right]

    print(f"Found {type} at {coordinates}")