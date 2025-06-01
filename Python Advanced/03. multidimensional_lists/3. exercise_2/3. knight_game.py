n = int(input())

chess_board = []
knights = [] # [[1, 2], [3, 4],...]

for row in range(n):
    chess_board.append(list(input()))
    for column in range(n):
        if chess_board[row][column] == 'K':
            knights.append([row, column])

removed_knights = 0
possible_moves = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))

while True:
    max_hits = 0
    max_knight = [0, 0] # position of knight with most possible hits

    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            next_row = k_row + move[0]
            next_col = k_col + move[1]
            if 0 <= next_row < n and 0 <= next_col < n:
                if chess_board[next_row][next_col] == 'K':
                    hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break

    knights.remove(max_knight)
    chess_board[max_knight[0]][max_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)