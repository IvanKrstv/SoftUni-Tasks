first_symbol = input()
second_symbol = input()
string = input()
total_sum = 0

for char in string:
    if ord(first_symbol) < ord(char) < ord(second_symbol):
        total_sum += ord(char)

print(total_sum)