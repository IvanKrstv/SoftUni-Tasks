contests = {}
results = {}

while True:
    current_contest = input()
    if current_contest == "end of contests":
        break

    contest, password = current_contest.split(":")
    contests[contest] = password

while True:
    info = input()
    if info == "end of submissions":
        break

    contest, password, username, points = info.split("=>")
    points = int(points)

    if contest in contests.keys() and password == contests[contest]:
        if username not in results.keys():
            results[username] = {}
        if contest not in results[username].keys():
            results[username][contest] = 0
        if points > results[username][contest]:
            results[username][contest] = points

# Determine best_candidate
best_candidate = username
for name, data in results.items():
    if sum(results[best_candidate].values()) < sum(data.values()):
        best_candidate = name

print(f"Best candidate is {best_candidate} with total {sum(results[best_candidate].values())} points.\nRanking:")

for name in list(sorted(results.keys())): # sorted list with usernames alphabetically
    print(f"{name}")
    sorted_dict = {k: v for k, v in sorted(results[name].items(), key=lambda item: item[1], reverse=True)}
    for contest, point in sorted_dict.items():
        print(f"#  {contest} -> {point}")