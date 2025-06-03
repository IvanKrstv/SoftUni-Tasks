import os

files = {}
directory = '../'


def get_files(folder, level):
    if level == -1:
        return
    for el in os.listdir(folder):
        f = os.path.join(folder, el)
        if os.path.isfile(f):
            extension = os.path.splitext(el)[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(el)
        else:
            get_files(f, level - 1)


get_files(directory, 1)

with open(os.path.join(directory, 'report.txt'), 'w') as f:
    for ext, file_names in sorted(files.items()):
        f.write(f'{ext}\n')
        for file_name in sorted(file_names):
            f.write(f'- - - {file_name}\n')