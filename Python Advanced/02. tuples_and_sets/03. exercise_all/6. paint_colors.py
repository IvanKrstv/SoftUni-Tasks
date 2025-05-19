from collections import deque

string = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

found_colors = []

while string:
    first = string.popleft()
    last = string.pop() if string else ''

    for res in (first + last, last + first):
        if res in main_colors or res in secondary_colors:
            found_colors.append(res)
            break
    else:
        if len(first) > 1:
            string.insert(len(string) // 2, first[:-1])
        if len(last) > 1:
            string.insert(len(string) // 2, last[:-1])

for color in found_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in found_colors:
                found_colors.remove(color)
                break
print(found_colors)