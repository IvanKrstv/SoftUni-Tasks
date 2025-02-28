numbers = [int(element) for element in input().split()]

def exchange(com):
    index = int(com[1])
    return numbers[index + 1:] + numbers[:index + 1]

def max_even_or_odd(com):
    even_or_odd = com[1]
    parity = 0 if even_or_odd == "even" else 1

    index_max = None
    for index in range(len(numbers)):
        if numbers[index] % 2 == parity:
            if index_max is None or numbers[index] >= numbers[index_max]:
                index_max = index

    if index_max is None:
        return "No matches"
    return index_max

def min_even_or_odd(com):
    even_or_odd = com[1]
    parity = 0 if even_or_odd == "even" else 1

    index_min = None
    for index in range(len(numbers)):
        if numbers[index] % 2 == parity:
            if index_min is None or numbers[index] <= numbers[index_min]:
                index_min = index

    if index_min is None:
        return "No matches"
    return index_min

def first(lst, count, parity):
    if int(count) > len(lst):
        return "Invalid count"
    else:
        filtered = [x for x in lst if x % 2 == parity]
        return filtered[:int(count)]

def last (lst, count, parity):
    if int(count) > len(lst):
        return "Invalid count"
    else:
        filtered = [x for x in lst if x % 2 == parity]
        return filtered[-int(count):]


while True:
    command = input()
    if command == "end":
        break
    command = command.split()
    result = None
    if command[0] == "exchange":
        if int(command[1]) >= len(numbers) or int(command[1]) < 0:
            print("Invalid index")
            continue
        numbers = exchange(command)
    elif command[0] == "max":
        result = max_even_or_odd(command)
    elif command[0] == "min":
        result = min_even_or_odd(command)
    elif command[0] == "first":
        parity = 0 if command[2] == "even" else 1
        result = first(numbers, command[1], parity)
    elif command[0] == "last":
        parity = 0 if command[2] == "even" else 1
        result = last(numbers, command[1], parity)

    if result is not None:
        print(result)
print(numbers)