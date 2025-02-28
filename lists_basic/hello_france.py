items = input().split("|")
budget = float(input())
profits = []
total_profit = 0
new_prices = 0
for element in items:
    item = element.split("->")
    type_item = item[0]
    price = float(item[1])
    if budget < price:
        continue
    if (type_item == "Clothes" and price <= 50) or (type_item == "Shoes" and price <= 35) or (type_item == "Accessories" and price <= 20.5):
        budget -= price
        new_price = price * 1.4
        total_profit += new_price - price
        new_prices += new_price
        profits.append(f"{new_price:.2f}")

print(" ".join(profits))
print(f"Profit: {total_profit:.2f}")
if budget + new_prices >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")