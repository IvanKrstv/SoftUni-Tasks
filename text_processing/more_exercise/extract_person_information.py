n = int(input())

for i in range(n):
    line = input()
    if "@" in line:
        index_1 = line.index("@")
        index_2 = line.index("|")
        index_3 = line.index("#")
        index_4 = line.index("*")
        name = line[index_1 + 1:index_2]
        age = int(line[index_3 + 1:index_4])
        print(f"{name} is {age} years old.")