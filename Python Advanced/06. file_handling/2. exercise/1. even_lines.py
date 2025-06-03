import os
path = os.path.join('..', 'ex_files', 'text.txt')

symbols = {"-", ",", ".", "!", "?"}
with open(path) as f:
    line_number = 0
    for line in f:
        if line_number % 2 == 0:
            for symbol in symbols:
                line = line.replace(symbol, '@')
            line_list = line.split()
            print(' '.join(word for word in line_list[::-1]))
        line_number += 1
