# Exceptions
class ColumnNotInRange(Exception):
    pass

class ColumnIsFull(Exception):
    pass


# Initialization of global consts
rows = 6
cols = 7
SLOTS_TO_WIN = 4


# Functions
def start_message() -> dict:
    print('Welcome to the "Connect four game!"'
          '\nPlease enter your names.')
    pl1 = input("First players's name: ")
    pl2 = input("Second players's name: ")

    return {1: pl1, 2: pl2}

def print_matrix(mtx: list[list]):
    print()
    for i in range(rows):
        print(mtx[i])
    print()

def valid_column(mtx, x: str):
    try:
        x = int(x) - 1
        if x not in range(cols):
            raise ColumnNotInRange
        if is_column_full(mtx, x):
            raise ColumnIsFull
    except (ValueError, ColumnNotInRange):
        print(f'The column has to be a number in the range between 1 and {cols}')
        return False
    except ColumnIsFull:
        print(f'Column {x + 1} is already full. Please choose another one!')
        return False
    return True

def is_column_full(mtx, col: int):
    return mtx[0][col] != 0

def player_move(mtx, col):
    for r in range(rows - 1, -1, -1):
        if mtx[r][col] == 0:
            return r
    return -1

def is_winner(mtx, r, c, pl_turn, slots):
    return any([
        is_row_winner(mtx, r, c, pl_turn, slots),
        is_col_winner(mtx, r, c, pl_turn, slots),
        is_main_diagonal(mtx, r, c, pl_turn, slots),
        is_secondary_diagonal(mtx, r, c, pl_turn, slots)
    ])

def is_player_num(mtx, r, c, pl_num):
    try:
        return mtx[r][c] == pl_num
    except IndexError:
        return False

def is_row_winner(mtx, r, c, pl_turn, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(mtx, r, c + idx, pl_turn):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(mtx, r, c - idx, pl_turn):
            filled += 1
        else:
            break

    return filled >= slots

def is_col_winner(mtx, r, c, pl_turn, slots):
    return all(is_player_num(mtx, r + i, c, pl_turn) for i in range(slots))

def is_main_diagonal(mtx, r, c, pl_turn, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(mtx, r + idx, c + idx, pl_turn):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(mtx, r - idx, c - idx, pl_turn):
            filled += 1
        else:
            break

    return filled >= slots

def is_secondary_diagonal(mtx, r, c, pl_turn, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(mtx, r - idx, c + idx, pl_turn):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(mtx, r + idx, c - idx, pl_turn):
            filled += 1
        else:
            break

    return filled >= slots

def main():
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    counter = 0
    players_dict = start_message()

    while True:
        player_turn = 2 if counter % 2 != 0 else 1
        if counter == rows * cols:
            print("The game is draw.")
            break

        column = input(f'{players_dict[player_turn]}, please choose a column: ')
        while not valid_column(matrix, column):
            column = input(f'{players_dict[player_turn]}, please choose a column: ')
        column = int(column) - 1

        row = player_move(matrix, column)
        matrix[row][column] = player_turn
        print_matrix(matrix)

        if is_winner(matrix, row, column, player_turn, SLOTS_TO_WIN):
            print(f'The winner is {players_dict[player_turn]}')
            break

        counter += 1

    # Ask to play again
    play_again = input("\nWould you like to play again? Yes or No: ").lower()
    if play_again in {'yes', 'ye', 'y'}:
        print()
        return 1
    else:
        print("Goodbye! Have a nice day!")
        return -1


if __name__ == '__main__':
    answer = 0
    while answer != -1:
        answer = main()