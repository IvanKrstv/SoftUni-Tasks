stack = []
n = int(input())

for i in range(n):
    query = input()
    if query.startswith('1'):
        number = int(query.split()[1])
        stack.append(number)
    elif stack:
        if query == '2':
            stack.pop()
        elif query == '3':
            print(max(stack))
        elif query == '4':
            print(min(stack))

print(', '.join((str(x) for x in stack[::-1])))