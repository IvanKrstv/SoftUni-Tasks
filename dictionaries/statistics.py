stock = {}

while True:
    info = input().split(": ")
    if info[0] == "statistics":
        break

    product, quantity = info[0], int(info[1])
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

print("Products in stock:")
for key, value in stock.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(stock.keys())}"
      f"\nTotal Quantity: {sum(stock.values())}")
