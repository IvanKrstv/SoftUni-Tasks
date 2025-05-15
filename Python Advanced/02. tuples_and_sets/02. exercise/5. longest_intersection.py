longest_intersection = set()

for _ in range(int(input())):
    first_part, second_part = input().split('-')
    first_start, first_end = tuple(map(int,first_part.split(',')))
    second_start, second_end = tuple(map(int, second_part.split(',')))

    first_set = set(num for num in range(first_start, first_end + 1))
    second_set = set(num for num in range(second_start, second_end + 1))
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in (sorted(longest_intersection)))}] with length {len(longest_intersection)}")