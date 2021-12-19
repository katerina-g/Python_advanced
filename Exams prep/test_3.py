n = int(input())
matrix = []
p_pos = []
is_won = False
commands_count = int(input())
for row in range(n):
    line = [x for x in input()]
    if "f" in line:
        p_pos = [row, line.index("f")]
    matrix.append(line)

for i in range(commands_count):
    command = input()
    positions = {"up": [-1, 0],
                 "down": [+1, 0],
                 "left": [0, -1],
                 "right": [0, +1],
                 }
    move = positions[command]
    new_p_row = int(p_pos[0]) + int(move[0])
    new_p_col = int(p_pos[1]) + int(move[1])
    next_pos = [new_p_row, new_p_col]
    next_two = [int(p_pos[0]) + int(move[0] + int(move[0])), int(p_pos[1]) + int(move[1] + int(move[1]))]
    if matrix[new_p_row][new_p_col] == "-":
        matrix[p_pos[0]][p_pos[1]] = "-"
        matrix[new_p_row][new_p_col] = "f"
        p_pos = next_pos
    elif matrix[new_p_row][new_p_col] == "F":
        is_won = True
        matrix[p_pos[0]][p_pos[1]] = "-"
        matrix[new_p_row][new_p_col] = "f"
        p_pos = next_pos
        break
    elif matrix[new_p_row][new_p_col] == "B":
        matrix[p_pos[0]][p_pos[1]] = "-"
        p_pos = next_two
    elif matrix[new_p_row][new_p_col] == "T":
        p_pos = p_pos
if is_won:
    print("Player won!")
else:
    print("Player lost!")
[print(''.join(row)) for row in matrix]