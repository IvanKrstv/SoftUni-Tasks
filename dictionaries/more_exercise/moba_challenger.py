players_pool = {}

def check_positions(players_pool, player1, player2):
    for position_first in players_pool[player1].keys():
        for position_second in players_pool[player2].keys():
            if position_first == position_second:
                if sum(players_pool[player1].values()) > sum(players_pool[player2].values()):
                    del players_pool[player2]
                    return players_pool
                elif sum(players_pool[player1].values()) < sum(players_pool[player2].values()):
                    del players_pool[player1]
                    return players_pool
    return players_pool

while True:
    command = input()
    if command == "Season end":
        break

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in players_pool:
            players_pool[player] = {}
        if position not in players_pool[player]:
            players_pool[player][position] = skill
        else:
            if skill > players_pool[player][position]:
                players_pool[player][position] = skill

    else:
        player1, player2 = command.split(" vs ")
        if player1 not in players_pool.keys() or player2 not in players_pool.keys():
            continue

        players_pool = check_positions(players_pool, player1, player2)

# Sorted dictionary for total points in descending order and players in ascending
sorted_players = {k: v for (k, v) in sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0]))}

for player, info in sorted_players.items():
    print(f"{player}: {sum(players_pool[player].values())} skill")

    sorted_dict = {k: v for (k, v) in sorted(players_pool[player].items(), key=lambda x: (-x[1], x[0]))} # Sorted points per role and roles
    for position, skill in sorted_dict.items():
        print(f"- {position} <::> {skill}")