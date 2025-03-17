import re

string = input()
pattern = r'(\d{2})([\.\-\/])([A-Z][a-z]{2})\2(\d{4})\b'

dates = re.finditer(pattern, string)
for date in dates:
    day, separator, month, year = date.groups()
    print(f"Day: {day}, Month: {month}, Year: {year}")

# 2
'''dates = re.findall(pattern, string)
for date in dates:
    day, month, year = date[0], date[2], date[3]

    print(f"Day: {day}, Month: {month}, Year: {year}")'''