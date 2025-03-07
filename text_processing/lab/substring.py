string1 = input()
string2 = input()

while string1 in string2:
    string2 = string2.replace(string1, "")

print(string2)