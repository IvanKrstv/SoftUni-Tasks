def grocery_store(**kwargs):
    result = ''
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        result += f'{key}: {value}\n'

    return result


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

