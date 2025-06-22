universe = {int(x) for x in input().split(', ')}
subsets = [set(int(x) for x in input().split(', ')) for _ in range(int(input()))]
needed_sets = []
remaining_sets = subsets.copy()

while universe and remaining_sets:
    best_set = max(remaining_sets, key=lambda x: len(universe.intersection(x)))
    if not universe.intersection(best_set):
        break
    needed_sets.append(best_set)
    universe -= set(best_set)
    remaining_sets.remove(best_set)


print(f'Sets to take ({len(needed_sets)}):')
for set in needed_sets:
    set_string = f'{", ".join(str(x) for x in sorted(set))}'
    print('{ ' + set_string + ' }')