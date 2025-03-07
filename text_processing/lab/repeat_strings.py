result = ""
words = input().split()

for i in range(len(words)):
    result += words[i] * len(words[i])

print(result)