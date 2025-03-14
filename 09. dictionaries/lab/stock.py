information = input().split()
stock = {}

for i in range(0, len(information), 2):
    key = information[i]
    value = information[i + 1]
    stock[key] = int(value)

for product in input().split():
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")