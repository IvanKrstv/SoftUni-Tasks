from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk_cups = deque(int(x) for x in input().split(', '))
milkshakes = 0

while milkshakes < 5 and chocolates and milk_cups:
    while chocolates and chocolates[-1] <= 0:
        chocolates.pop()
    while milk_cups and milk_cups[0] <= 0:
        milk_cups.popleft()

    if not chocolates or not milk_cups:
        break

    current_chocolate = chocolates.pop()
    current_cup = milk_cups.popleft()

    if current_cup == current_chocolate:
        milkshakes += 1
    else:
        milk_cups.append(current_cup)
        current_chocolate -= 5
        chocolates.append(current_chocolate) if current_chocolate > 0 else None

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")