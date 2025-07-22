class store_results:
    out_file = 'results.txt'
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open(self.out_file, 'a+') as f:
            result = self.func(*args, **kwargs)
            f.write(f"Function '{self.func.__name__}' was called. Result: {result}\n")

        return result

class store_results_with_params:
    def __init__(self, out_file):
        self.out_file = out_file

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with open(self.out_file, 'a+') as f:
                result = func(*args, **kwargs)
                f.write(f"Function '{func.__name__}' was called. Result: {result}\n")

        return wrapper

@store_results
def add(a, b):
    return a + b

@store_results_with_params('result.txt')
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)