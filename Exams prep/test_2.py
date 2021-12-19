from math import floor

movements = {"up": [-1, 0],
             "down": [+1, 0],
             "left": [0, -1],
             "right": [0, + 1],
             }

n = int(input())
matrix = []
player_pos = []
is_win = True
coins = 0
path = []
for row in range(n):
    line = input().split()
    if "P" in line:
        player_pos = [row, line.index("P")]
    matrix.append(line)

while True:
    command = input()
    if command in movements:
        move = movements[command]
        new_p_row = int(player_pos[0]) + int(move[0])
        new_p_col = int(player_pos[1]) + int(move[1])
        next_pos = [new_p_row, new_p_col]
        if 0 <= new_p_row < n and 0 <= new_p_col < n:
            if matrix[new_p_row][new_p_col] == "X":
                coins = floor(coins / 2)
                is_win = False
                break
            else:
                coins += int(matrix[new_p_row][new_p_col])
                player_pos = next_pos
                path.append(player_pos)
                if coins >= 100:
                    break
        else:
            coins = floor(coins / 2)
            is_win = False
            break

if is_win:
    print(f"You won! You've collected {coins} coins.")
    print(f"Your path:")
    print('\n'.join(list(str(el) for el in path)))
else:
    print(f"Game over! You've collected {coins} coins.")
    print(f"Your path:")
    print("\n".join(list(str(el) for el in path)))
