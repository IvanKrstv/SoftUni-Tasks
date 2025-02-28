items = {"shards": 0, "fragments": 0, "motes": 0}
obtained_item = ""

while obtained_item == "":
    info = input().lower().split()
    quantities = [info[index] for index in range(len(info)) if index % 2 == 0]
    elements = [info[index] for index in range(len(info)) if index % 2 != 0]

    for i in range(len(elements)):
        if elements[i] not in items.keys():
            items[elements[i]] = 0
        items[elements[i]] += int(quantities[i])

        if items["shards"] >= 250:
            items["shards"] -= 250
            obtained_item = "Shadowmourne"
            break
        elif items["fragments"] >= 250:
            items["fragments"] -= 250
            obtained_item = "Valanyr"
            break
        elif items["motes"] >= 250:
            items["motes"] -= 250
            obtained_item = "Dragonwrath"
            break

print(f"{obtained_item} obtained!")
for key, value in items.items():
    print(f"{key}: {value}")

