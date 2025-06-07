def boarding_passengers(ship_capacity: int, *args):
    guests = {}
    all_passengers_boarded = True
    for arg in args:
        if ship_capacity == 0:
            all_passengers_boarded = False
            break

        number_passengers, benefits_program = int(arg[0]), arg[1]
        if number_passengers > ship_capacity:
            all_passengers_boarded = False
            continue

        if benefits_program not in guests:
            guests[benefits_program] = 0
        guests[benefits_program] += number_passengers
        ship_capacity -= number_passengers

    sorted_guests = dict(sorted(guests.items(), key=lambda x: (-x[1], x[0])))

    output_message = f'Boarding details by benefit plan:'
    for plan, number_guests in sorted_guests.items():
        output_message += f'\n## {plan}: {number_guests} guests'
    if all_passengers_boarded:
        output_message += '\nAll passengers are successfully boarded!'
    elif ship_capacity == 0 and not all_passengers_boarded:
        output_message += '\nBoarding unsuccessful. Cruise ship at full capacity.'
    elif ship_capacity > 0 and not all_passengers_boarded:
        output_message += f'\nPartial boarding completed. Available capacity: {ship_capacity}.'

    return output_message

print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
