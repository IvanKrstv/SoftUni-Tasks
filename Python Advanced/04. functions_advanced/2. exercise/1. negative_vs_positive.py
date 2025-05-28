def info(*args):
    negatives = sum([arg for arg in args if arg < 0])
    positives = sum([arg for arg in args if arg > 0])

    final_string = f'{negatives}\n{positives}\n'

    if abs(negatives) > abs(positives):
        final_string += "The negatives are stronger than the positives"
    elif abs(positives) > abs(negatives):
        final_string += "The positives are stronger than the negatives"

    return final_string


nums = [int(x) for x in input().split()]
print(info(*nums))