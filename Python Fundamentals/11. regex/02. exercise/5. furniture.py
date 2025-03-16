import re

pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)'
furniture_names = []
total_cost = 0

while True:
    line = input()
    if line == "Purchase":
        break

    result = re.search(pattern, line)
    if result:
        name, price, quantity = result.groups()
        price, quantity = float(price), int(quantity)

        total_cost += price * quantity
        furniture_names.append(name)

print("Bought furniture:")
for name in furniture_names:
    print(name)
print(f"Total money spend: {total_cost:.2f}")