from collections import deque

quantity_food = int(input())
queue = deque(int(x) for x in input().split())

print(max(queue))

while queue:
    current_order = queue[0]
    if current_order > quantity_food:
        break
    else:
        queue.popleft()
        quantity_food -= current_order

if not queue:
    print("Orders complete")
else:
    print(f"Orders left:", *queue)