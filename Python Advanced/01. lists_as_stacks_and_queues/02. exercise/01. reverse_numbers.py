data = [int(x) for x in input().split()]
stack = []
while data:
    stack.append(data.pop())

for el in stack:
    print(el, end=" ")