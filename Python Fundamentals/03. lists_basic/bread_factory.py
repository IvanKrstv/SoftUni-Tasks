energy = 100
coins = 100
all_events = input().split("|")
bakery_is_open = True
for element in all_events:
    new_element = element.split("-")
    event = new_element[0]
    number = int(new_element[1])
    if event == "rest":
        new_energy = energy + number
        if new_energy > 100:
            new_energy = 100
        print(f"You gained {new_energy - energy} energy.")
        energy += new_energy - energy
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            bakery_is_open = False
            break

if bakery_is_open:
    print(f"Day completed!"
          f"\nCoins: {coins}"
          f"\nEnergy: {energy}")
else:
    print(f"Closed! Cannot afford {event}.")