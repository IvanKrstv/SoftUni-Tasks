import os

path = os.path.join('..', 'ex_files', 'ex_2_input.txt')
path_output = os.path.join('..', 'ex_files', 'ex_2_output.txt')
final_lines = []
with open(path) as input_file, open(path_output, 'w') as output_file:
    for line_number, line in enumerate(input_file):
        count_letters = 0
        count_punc = 0
        for char in line.rstrip('\n'):
            if char.isalpha():
                count_letters += 1
            elif char == ' ' or char.isdigit():
                continue
            else:
                count_punc += 1
        final_lines.append(f'Line {line_number + 1}: {line} ({count_letters})({count_punc})')

    output_file.write('\n'.join(final_lines))