from collections import deque

string = input().split()
numbers = deque()
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: int(x / y)
}

for el in string:
    if el in operators:
        operation = operators[el]
        result = numbers.popleft()
        while numbers:
            result = operation(result, numbers.popleft())
        numbers.appendleft(result) # result is stored as numbers[0]
    else:
        el = int(el)
        numbers.append(int(el))

print(numbers[0]) # result