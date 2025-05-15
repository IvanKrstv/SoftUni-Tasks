n, m = input().split()
n, m = int(n), int(m)
set_n = set(input() for _ in range(n))
set_m = set(input() for _ in range(m))

print(*set_n.intersection(set_m), sep='\n')

