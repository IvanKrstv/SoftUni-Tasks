string = input()
stack = []
parentheses = {')': '(', ']': '[', '}': '{'}
balanced = True

for char in string:
    if char in parentheses.values():
        stack.append(char)
    else:
        if stack and stack[-1] == parentheses[char]:
            stack.pop()
        else:
            balanced = False
            break

print('YES') if balanced else print('NO')