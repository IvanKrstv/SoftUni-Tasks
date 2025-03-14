n = int(input())
my_dict = {}
for i in range(2 * n):
    if i % 2 == 0:
        word = input()
        if word not in my_dict:
            my_dict[word] = []
    else:
        synonym = input()
        my_dict[word].append(synonym)

for key, value in my_dict.items():
    print(f"{key} - {', '.join(value)}")