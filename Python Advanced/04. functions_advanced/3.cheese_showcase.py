def sorting_cheeses(**kwargs):
    final_string = ''
    for key, list in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        final_string += key + '\n'
        for el in sorted(list, reverse=True):
            final_string += f'{el}\n'

    return final_string

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)