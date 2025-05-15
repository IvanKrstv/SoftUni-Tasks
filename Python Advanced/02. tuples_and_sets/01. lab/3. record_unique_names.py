n = int(input())
s = set()
for _ in range(n):
    name = input()
    s.add(name)

for name in s:
    print(name)