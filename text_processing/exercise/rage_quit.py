string = input()
current_message = ""
final_message = ""
unique_symbols = []

for i in range(len(string)):
    if not string[i].isdigit():
        current_message += string[i]
        if string[i].lower() not in unique_symbols:
            unique_symbols.append(string[i].lower())

    elif string[i].isdigit() and not string[i - 1].isdigit():
        if not i + 1 >= len(string) and string[i + 1].isdigit():
            n = int(string[i:i + 2])
        else:
            n = int(string[i])
        final_message += current_message.upper() * n
        current_message = ""

print(f"Unique symbols used: {len(unique_symbols)}"
      f"\n{final_message}")