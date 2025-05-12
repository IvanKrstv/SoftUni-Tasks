expression = input()
stack_indexes = []

for index in range(len(expression)):
    if expression[index] == '(':
        stack_indexes.append(index)
    elif expression[index] == ')':
        first_index = stack_indexes.pop()
        print(expression[first_index:index + 1])
