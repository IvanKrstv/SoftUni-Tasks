def sort_games(*args, **kwargs):
    console_games = []
    pc_games = []
    for arg in args:
        platform = arg[0]
        game_title = arg[1]
        for id, game in kwargs.items():
            if game_title == game:
                if platform == 'console':
                    console_games.append((id, game_title))
                elif platform == 'pc':
                    pc_games.append((id, game_title))

    result = ''
    if console_games:
        result += 'Console Games:\n'
        for game in sorted(console_games, key=lambda x: x[0]):
            id, title = game[0], game[1]
            result += f'>>>{id[:-4]}: {title}\n'
    if pc_games:
        result += 'PC Games:\n'
        for game in sorted(pc_games, key=lambda x: x[0], reverse=True):
            id, title = game[0], game[1]
            result += f'<<<{id[:-4]}: {title}\n'

    return result

print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))



