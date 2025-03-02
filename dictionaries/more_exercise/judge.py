contests = {}
results = {}

while True:
    command = input()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}
    if username not in contests[contest]:
        contests[contest][username] = points
    else:
        if points > contests[contest][username]:
            contests[contest][username] = points

    if username not in results:
        results[username] = 0
    results[username] = sum(contests[c][username] for c in contests if username in contests[c])

for contest in contests.keys():
    sorted_dict = {key:value for key, value in sorted(contests[contest].items(), key=lambda item: (-item[1], item[0]))} # Sort by points descending, then name ascending
    print(f"{contest}: {len(contests[contest].keys())} participants")
    i = 1
    for k, v in sorted_dict.items():
        print(f"{i}. {k} <::> {v}")
        i+=1

print("Individual standings:")
sorted_results = {key:value for key, value in sorted(results.items(), key=lambda item: (-item[1], item[0]))} # Sort by total points descending, then name ascending
i = 1
for username, points in sorted_results.items():
    print(f"{i}. {username} -> {points}")
    i+=1