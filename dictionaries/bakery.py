information = input().split()
dic = {}
for i in range(0, len(information) , 2):
    key = information[i]
    value = information[i + 1]
    dic[key] = int(value)

print(dic)