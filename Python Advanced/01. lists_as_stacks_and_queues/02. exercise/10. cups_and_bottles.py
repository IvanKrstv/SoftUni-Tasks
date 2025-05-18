from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())

wasted_liters = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    current_cup_full = current_cup
    current_cup -= current_bottle
    if current_bottle > current_cup_full:
        wasted_liters += abs(current_cup)

    if current_cup > 0:
        cups.appendleft(current_cup)

if not cups:
    print(f"Bottles: ", end='')
    while bottles:
        print(f'{bottles.pop()} ')
else:
    print(f'Cups: {" ".join([str(x) for x in cups])}')

print(f"Wasted litters of water: {wasted_liters}")