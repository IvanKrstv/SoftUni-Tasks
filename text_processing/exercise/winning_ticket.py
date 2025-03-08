winning_symbols = ('@', '#', '$', '^')

def is_winning(ticket):
    if not len(ticket) == 20:
        return "invalid ticket"

    first_part = ticket[:10]
    second_part = ticket[10:]

    for symbol in winning_symbols:
        if ticket.count(symbol) == 20:
            return f'ticket "{ticket}" - 10{symbol} Jackpot!'

        for possible_length in range(9, 5, -1):
            sequence = symbol * possible_length
            if sequence in first_part and sequence in second_part:
                return f'ticket "{ticket}" - {possible_length}{symbol}'

    return f'ticket "{ticket}" - no match'

tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(is_winning(ticket))

