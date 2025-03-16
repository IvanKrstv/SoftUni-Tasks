words = input().lower().split()
my_dict = {}
for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

for key, value in my_dict.items():
    if value % 2 != 0:
        print(key.lower(), end=" ")