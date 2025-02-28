to_do = []

while True:
    task = input()
    if task == "End":
        break
    to_do.append(task)

sorted_to_do = sorted(to_do, key=lambda x:int(x.split("-")[0]))
print([task.split("-")[1] for task in sorted_to_do])
