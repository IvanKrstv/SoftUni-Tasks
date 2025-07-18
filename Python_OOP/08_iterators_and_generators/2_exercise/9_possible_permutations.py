import itertools

def possible_permutations(numbers):
    for perm in itertools.permutations(numbers):
        yield list(perm)

[print(n) for n in possible_permutations([1, 2, 3])]