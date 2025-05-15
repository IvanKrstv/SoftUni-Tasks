even_set = set()
odd_set =set()

for i in range(int(input())):
    current_row = i + 1
    name = input()
    result = int(sum(ord(letter) for letter in name) / current_row)

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(even_set) == sum(odd_set):
    print(*(odd_set.union(even_set)), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*(odd_set - even_set), sep=', ')
else:
    print(*(odd_set.symmetric_difference(even_set)), sep=', ')