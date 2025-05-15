elements = set()
for _ in range(int(input())):
    current_els = input().split()
    for el in current_els:
        elements.add(el)

print(*elements, sep='\n')