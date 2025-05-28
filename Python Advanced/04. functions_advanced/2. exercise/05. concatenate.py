def concatenate(*args, **kwargs):
    string = ''
    for arg in args:
        string += arg

    for key, value in kwargs.items():
        if str(key) in string:
            string = string.replace(key, value)

    return string

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))