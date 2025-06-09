import logic

fibonacci_sequence = []
while True:
    command = input().split()
    if command[0] == 'Stop':
        break

    if command[0] == 'Create':
        number = int(command[2])
        fibonacci_sequence.clear()
        for i in range(number):
            fibonacci_sequence.append(logic.sequence(i))
        print(*fibonacci_sequence)

    elif command[0] == 'Locate':
        number = int(command[1])
        print(logic.locate(number, fibonacci_sequence))