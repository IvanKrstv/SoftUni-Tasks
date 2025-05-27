def operate(operator, *args):
    result = args[0]
    for arg in args[1:]:
        if operator == '+':
            result += arg
        elif operator == '-':
            result -= arg
        elif operator == '*':
            result *= arg
        elif operator == '/':
            if arg == 0:
                continue
            result /= arg

    return result

print(operate("*", 3, 4))