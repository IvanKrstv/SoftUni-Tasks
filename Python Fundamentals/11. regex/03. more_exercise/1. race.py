import re

participants = input().split(", ")
race = {}

pattern_name = r'[A-Za-z]+'
pattern_distance = r'\d'

while True:
    line = input()
    if line == "end of race":
        break

    current_name = "".join(re.findall(pattern_name, line))
    distance = sum([int(x) for x in re.findall(pattern_distance, line)])

    if current_name in participants:
        if current_name not in race.keys():
            race[current_name] = 0
        race[current_name] += distance

'''sorted_dict = dict(sorted(race.items(), key=lambda x: -x[1])[:3])
place = 1
text = "1st"
for name, distance in sorted_dict.items():
    if place == 2:
        text = "2nd"
    elif place == 3:
        text = "3rd"

    print(f"{text} place: {name}")
    place += 1'''

top_racers = sorted(race.items(), key=lambda x: -x[1])[:3]
places = ["1st", "2nd", "3rd"]
for i, (name, distance) in enumerate(top_racers):
    print(f"{places[i]} place: {name}")