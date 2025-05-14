numbers = tuple(float(x) for x in input().split())
printed_nums = []

for num in numbers:
    if num not in printed_nums:
        print(f"{num:.1f} - {numbers.count(num)} times")
        printed_nums.append(num)