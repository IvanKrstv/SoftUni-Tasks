def logged(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        func_name = func.__name__
        arguments = list(arg for arg in args)
        arguments += [kwarg for kwarg in kwargs]
        return (f"you called {func_name}{tuple(arguments)}\n"
                f"it returned {result}")
    return wrapper

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))