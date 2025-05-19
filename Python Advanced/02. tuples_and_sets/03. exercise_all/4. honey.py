from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
given_operators = deque(input().split())

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else 0
}
total_honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nec = nectar.pop()

    if current_nec >= current_bee:
        op = given_operators.popleft()
        total_honey += abs(operations[op](current_bee, current_nec))
    else:
        bees.appendleft(current_bee)
        continue

print(f"Total honey made: {total_honey}")
print(f"Bees left: {', '.join(str(x) for x in bees)}") if bees else None
print(f"Nectar left: {', '.join(str(x) for x in nectar)}") if nectar else None

