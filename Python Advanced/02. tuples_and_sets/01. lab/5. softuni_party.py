n = int(input())
guests = {'VIP': set(), 'Regular': set()}
guest_codes = [input() for _ in range(n)]

while True:
    code = input()
    if code == 'END':
        break

    if code.isalpha():
        guests['Regular'].add(code)
    else:
        guests['VIP'].add(code)

print(len(guest_codes) - len(guests['Regular']) - len(guests['VIP']))
didnt_came = tuple(sorted(code for code in guest_codes if code not in guests['Regular'] and code not in guests['VIP']))
print(*didnt_came, sep='\n')