set1 = {int(x) for x in input().split()}
set2 = {int(x) for x in input().split()}

def add(set, nums):
    set.update(nums)

def remove(set, nums):
    set.difference_update(nums)

def check_subset(set1, set2):
    return set1 < set2 or set2 < set1

for _ in range(int(input())):
    info = input().split()
    command = info[0]
    number_set = info[1]
    numbers = list(map(int, info[2:]))

    if command == 'Add':
        if number_set == 'First':
            add(set1, numbers)
        elif number_set == 'Second':
            add(set2, numbers)
    elif command == 'Remove':
        if number_set == 'First':
            remove(set1, numbers)
        elif number_set == 'Second':
            remove(set2, numbers)
    elif command == 'Check':
        print(check_subset(set1, set2))

print(*(sorted(set1)), sep=', ')
print(*(sorted(set2)), sep=', ')
