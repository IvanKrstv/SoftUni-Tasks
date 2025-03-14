statistics = {}
languages = {}

while True:
    command = input()
    if command == "exam finished":
        break
    if "banned" in command:
        del statistics[command.split("-")[0]]
        continue

    username, language, points = command.split("-")
    points = int(points)

    if username not in statistics.keys():
        statistics[username] = points
    else:
        if points > statistics[username]:
            statistics[username] = points

    if language not in languages.keys():
        languages[language] = 0
    languages[language] += 1

print("Results:")
for name, points in statistics.items():
    print(f"{name} | {points}")
print("Submissions:")
for language, submissions in languages.items():
    print(f"{language} - {submissions}")