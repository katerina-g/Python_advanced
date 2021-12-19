from math import floor


def is_valid(r, c, s):
    if 0 <= r < s and 0 <= c < s:
        return True
    return False


field = []
directions = {"up": [-1, 0],
              "down": [+1, 0],
              "left": [0, - 1],
              "right": [0, + 1]
              }
total_coins = 0
path = []

n = int(input())
pl_pos = []
for row_index in range(n):
    line = input().split()
    if "P" in line:
        pl_pos = [row_index, line.index("P")]
    field.append(line)

while True:
    command = input()
    if command in directions:
        dir_change = directions[command]
        next_row = pl_pos[0] + dir_change[0]
        next_col = pl_pos[1] + dir_change[1]
        next_pos = [next_row, next_col]
        if not is_valid(next_row, next_col, n) or field[next_row][next_col] == "X":
            total_coins = floor(total_coins / 2)
            print(f"Game over! You've collected {total_coins} coins.")
            break
        elif field[next_row][next_col] != "X":
            total_coins += int(field[next_row][next_col])
            pl_pos = next_pos
            path.append(pl_pos)
            if total_coins >= 100:
                print(f"You won! You've collected {total_coins} coins.")
                break
print("Your path:")
for el in path:
    print(el)





