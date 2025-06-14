def accommodate(*args, **kwargs):
    sorted_rooms = sorted(kwargs.items(), key=lambda x: (x[1], x[0]))
    rooms = {}
    unaccommodated_guests = 0
    for guest_group in args:
        for room in sorted_rooms:
            if room[1] >= guest_group:
                rooms[room[0][-3:]] = guest_group
                sorted_rooms.remove(room)
                break
        else:
            unaccommodated_guests += guest_group

    result = ''
    if rooms:
        result += f'A total of {len(rooms)} accommodations were completed!\n'
        for room_number, guests in sorted(rooms.items()):
            result += f'<Room {room_number} accommodates {guests} guests>\n'
    else:
        result += "No accommodations were completed!\n"

    if unaccommodated_guests > 0:
        result += f"Guests with no accommodation: {unaccommodated_guests}\n"
    if len(rooms) < len(kwargs):
        total_number_of_empty_rooms = len(kwargs) - len(rooms)
        result += f"Empty rooms: {total_number_of_empty_rooms}"

    return result


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))