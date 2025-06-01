n = 5
matrix = []
targets = 0
hit_targets = []
position = ()

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == 'A':
            position = (i, j)
        elif matrix[i][j] == 'x':
            targets += 1


possible_moves = {'down': (1, 0), 'up': (-1, 0), 'left': (0, -1), 'right': (0, 1)}

for _ in range(int(input())):
    command = input().split()
    action, direction = command[0], command[1]

    if action == 'move':
        steps = int(command[2])
        r = position[0] + possible_moves[direction][0] * steps
        c = position[1] + possible_moves[direction][1] * steps
        if 0 <= r < n and 0 <= c < n and matrix[r][c] == '.':
            matrix[r][c] = 'A'
            matrix[position[0]][position[1]] = '.'
            position = (r, c)


    elif action == 'shoot':
        r = position[0] + possible_moves[direction][0]
        c = position[1] + possible_moves[direction][1]
        while 0 <= r < n and 0 <= c < n:
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                targets -= 1
                hit_targets.append([r, c])
                break

            r += possible_moves[direction][0]
            c += possible_moves[direction][1]
        if targets == 0:
            print(f"Training completed! All {len(hit_targets)} targets hit.")
            break

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

for tar in hit_targets:
    print(tar)