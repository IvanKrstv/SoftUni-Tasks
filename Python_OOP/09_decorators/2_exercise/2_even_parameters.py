def even_parameters(func):

    def wrapper(*args, **kwargs):
        odd_numbers = ([arg for arg in args if not isinstance(arg, int) or arg % 2 != 0] +
                       [kwarg for kwarg in kwargs if not isinstance(kwarg, int) or kwarg % 2 != 0])
        if odd_numbers:
            return "Please use only even numbers!"
        result = func(*args, *kwargs)
        return result
    return wrapper

@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))