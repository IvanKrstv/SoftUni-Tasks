products_dict = {}

while True:
    current_product = input()
    if current_product == "buy":
        break

    product_name, price, quantity = current_product.split()

    if product_name not in products_dict.keys():
        products_dict[product_name] = [float(price), int(quantity)]
    else:
        products_dict[product_name][0] = float(price)
        products_dict[product_name][1] += int(quantity)

for key, value in products_dict.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")