from collections import deque

quantity = int(input())
queue = deque()

while True:
    name = input()
    if name == "Start":
        break

    queue.append(name)

while True:
    command = input()
    if command == "End":
        break

    if command.isdigit():
        liters = int(command)
        person_name = queue.popleft()
        if liters <= quantity:
            quantity -= liters
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    elif command.startswith('refill'):
        _, liters = command.split()
        liters = int(liters)
        quantity += liters

print(f"{quantity} liters left")
