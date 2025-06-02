with open('numbers.txt') as f:
    sum_nums = 0
    for line in f:
        sum_nums += int(line)

print(sum_nums)