def even_odd_filter(**kwargs):
    final_dict = {}
    for type, nums in kwargs.items():
        if type == 'even':
            final_dict[type] = [num for num in nums if num % 2 == 0]
        else:
            final_dict[type] = [num for num in nums if num % 2 != 0]

    return dict(sorted(final_dict.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

