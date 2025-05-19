from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents = {
    150: 'Doll', 250: 'Wooden train',
    300: 'Teddy bear', 400: 'Bicycle'
}

done = {}

while materials and magic:
    current_mat = materials[-1]
    current_magic = magic[0]
    total_magic_level = current_mat * current_magic

    if total_magic_level in presents:
        if presents[total_magic_level] not in done:
            done[presents[total_magic_level]] = 0
        done[presents[total_magic_level]] += 1
        materials.pop()
        magic.popleft()
    elif total_magic_level < 0:
        res = materials.pop() + magic.popleft()
        materials.append(res)
    elif total_magic_level > 0:
        magic.popleft()
        materials[-1] += 15
    else:
        if current_mat == 0:
            materials.pop()
        if current_magic == 0:
            magic.popleft()

if ('Doll' in done and 'Wooden train' in done) or ('Teddy bear' in done and 'Bicycle' in done):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}") if materials else None
print(f"Magic left: {', '.join(str(x) for x in magic)}") if magic else None
for toy, amount in sorted(done.items()):
    print(f"{toy}: {amount}")