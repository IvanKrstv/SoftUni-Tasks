import os

def create(file_name):
    open(file_name, 'w').close()

def add(file_name, content):
    with open(file_name, 'a') as file:
        file.write(f'{content}\n')

def replace(file_name, old_string, new_string):
    try:
        file = open(file_name, 'r+')
    except FileNotFoundError:
        print("An error occurred")
    else:
        text = file.read().replace(old_string, new_string)
        file.seek(0)
        file.truncate(0)
        file.write(text)
        file.close()

def delete(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


while True:
    command = input().split('-')
    if command[0] == 'End':
        break

    if command[0] == 'Create':
        create(command[1])
    elif command[0] == 'Add':
        add(command[1], command[2])
    elif command[0] == 'Replace':
        replace(*command[1:4])
    elif command[0] == 'Delete':
        delete(command[1])
