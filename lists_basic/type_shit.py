number_list = list(input())
first_list = []
second_list = []
third_list = []
fourth_list = []

for index in range(len(number_list), len(number_list) - 3, - 1):
    first_list.append(number_list[index - 1])
first_list.reverse()
if len(number_list) >= 4:
    for index in range(len(number_list) - 3, len(number_list) - 6, - 1):
        second_list.append(number_list[index - 1])
    second_list.reverse()
if  len(number_list) >= 7:
    for index in range(len(number_list) - 6, len(number_list) - 9, - 1):
        third_list.append(number_list[index - 1])
    third_list.reverse()
if len(number_list) >= 10:
    for index in range(len(number_list) - 9, 0, - 1):
        fourth_list.append(number_list[index - 1])
    fourth_list.reverse()

result = ""
if fourth_list:
   result += "".join(fourth_list) + ", "
if third_list:
    result += "".join(third_list) + ", "
if second_list:
    result += "".join(second_list) + ", "
result += "".join(first_list)

print(result)


