text = input()
n = int(input())
matrix = []

player_pos = []

dirs = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for row_index in range(n):
    current_row = list(input())
    if "P" in current_row:
        player_pos = [row_index, current_row.index("P")]

    matrix.append(current_row)


n_commands = int(input())

for _ in range(n_commands):
    command = input()
    direction_change = dirs[command]
    next_row = player_pos[0] + direction_change[0]
    next_col = player_pos[1] + direction_change[1]
    next_pos = [next_row, next_col]

    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == "-":
            matrix[player_pos[0]][player_pos[1]] = "-"
            player_pos = next_pos
            matrix[player_pos[0]][player_pos[1]] = "P"
        else:
            matrix[player_pos[0]][player_pos[1]] = "-"
            text += matrix[next_row][next_col]
            player_pos = next_pos
            matrix[player_pos[0]][player_pos[1]] = "P"
    else:
        text = text[:-1]

print(text)
[print(''.join(row)) for row in matrix]

