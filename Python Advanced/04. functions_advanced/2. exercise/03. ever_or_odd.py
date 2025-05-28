def even_odd(*args):
    final_list = [arg for arg in args[:-1] if arg % 2 == 0] if args[-1] == 'even' else [arg for arg in args[:-1] if arg % 2 != 0]

    return final_list

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))