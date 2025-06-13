from collections import deque

bees = deque(int(x) for x in input().split())
bee_eaters = [int(x) for x in input().split()]

BEES_PER_BEE_EATER = 7

while bees and bee_eaters:
    current_bees = bees.popleft()
    current_eaters = bee_eaters.pop()

    while current_eaters > 0 and current_bees > 0:
        current_bees -= BEES_PER_BEE_EATER
        if current_bees >= 0:
            current_eaters -= 1

    if current_bees == current_eaters:
        continue

    if current_bees <= 0:
        bee_eaters.append(current_eaters)
    elif current_eaters <= 0:
        bees.append(current_bees)

print('The final battle is over!')
if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees and not bee_eaters:
    print(f"Bee groups left: {', '.join(str(x) for x in bees)}")
elif not bees and bee_eaters:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters)}")