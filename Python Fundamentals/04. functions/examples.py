def sequence(lst):
    count_minus = 0
    for element in lst:
        if element == "0":
            return "zero"
        if "-" in element:
            count_minus += 1
    if count_minus % 2 == 0:
        return "positive"
    else:
        return "negative"

my_lst = []
for i in range(3):
    my_lst.append(input())

print(sequence(my_lst))