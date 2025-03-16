import re

pattern = r'%([A-Z][a-z]+)%[^\|\$\%\.]*<(\w+)>[^\|\$\%\.]*\|(\d+)\|[^\|\$\%\.0-9]*(\d+\.?\d*)\$'
total_income = 0

while True:
    line = input()
    if line == "end of shift":
        break

    match = re.search(pattern, line)

    if match:
        customer, product, count, price = match.groups()
        count, price = int(count), float(price)

        total_price = count * price
        total_income += total_price

        print(f"{customer}: {product} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")