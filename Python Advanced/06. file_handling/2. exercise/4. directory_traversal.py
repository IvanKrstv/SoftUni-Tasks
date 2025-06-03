import os

files = {}
directory = '../'

for el in os.listdir(directory):
    f = os.path.join(directory, el)
    if os.path.isfile(f):
        ext = el.split('.')[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(el)
    else:
        for element in os.listdir(f):
            filename = os.path.join(f, element)
            if os.path.isfile(filename):
                ext = element.split('.')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(element)

with open(os.path.join(directory, 'report.txt'), 'w') as f:
    for ext, file_names in sorted(files.items()):
        f.write(f'.{ext}\n')
        for file_name in sorted(file_names):
            f.write(f'- - - {file_name}\n')