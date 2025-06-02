try:
    f = open('text.txt')
except FileNotFoundError:
    print('File not found')
else:
    print('File found')