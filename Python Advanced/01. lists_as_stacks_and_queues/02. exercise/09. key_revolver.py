from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
value_of_the_intelligence = int(input())

used_bullets = 0
shot = 0

while locks and bullets:
    current_lock = locks.popleft()
    current_bullet = bullets.pop()

    used_bullets += 1
    shot += 1

    if current_bullet <= current_lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(current_lock)
    if used_bullets == gun_barrel_size and bullets:
        print('Reloading!')
        used_bullets = 0

money_earned = value_of_the_intelligence - shot * bullet_price
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}" )
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")