def calcs(num1, opp, num2):
    result = 0
    if opp == '/':
        result = num1 / num2
    elif opp == '*':
        result = num1 * num2
    elif opp == '-':
        result = num1 - num2
    elif opp == '+':
        result = num1 + num2
    elif opp == '^':
        result = pow(num1, num2)

    return f'{result:.2f}'