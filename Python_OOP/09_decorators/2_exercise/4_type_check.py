def type_check(some_type):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, some_type):
                    return "Bad Type"
            for kwarg in kwargs:
                if not isinstance(kwarg, some_type):
                    return "Bad Type"

            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))