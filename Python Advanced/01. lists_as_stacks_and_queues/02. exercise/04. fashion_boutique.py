clothes = [int(x) for x in input().split()]
capacity = int(input())

racks = 0

while clothes:
    racks += 1
    current_capacity = capacity
    while clothes and clothes[-1] <= current_capacity:
        current_capacity -= clothes.pop()

print(racks)