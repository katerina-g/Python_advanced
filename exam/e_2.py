def is_valid(r, c, s):
    if 0 <= r < s and 0 <= c < s:
        return True
    return False


movements = {"up": [-1, 0],
             "down": [+1, 0],
             "left": [0, - 1],
             "right": [0, + 1]
             }
n = int(input())
matrix = []
alice_pos = []
tea_bags = 0
is_party = True

for row in range(n):
    line = input().split()
    if "A" in line:
        alice_pos = [row, line.index("A")]
    matrix.append(line)

while True:
    command = input()
    move = movements[command]
    new_row = int(alice_pos[0]) + int(move[0])
    new_col = int(alice_pos[1] + int(move[1]))
    next_pos = [new_row, new_col]
    if not is_valid(new_row, new_col, n):
        matrix[alice_pos[0]][alice_pos[1]] = "*"
        is_party = False
        break
    if matrix[new_row][new_col] == "R":
        matrix[alice_pos[0]][alice_pos[1]] = "*"
        matrix[new_row][new_col] = "*"
        is_party = False
        break

    if matrix[new_row][new_col] == ".":
        matrix[alice_pos[0]][alice_pos[1]] = "*"
        alice_pos = next_pos
        matrix[alice_pos[0]][alice_pos[1]] = "A"
    elif matrix[new_row][new_col] == "*":
        matrix[alice_pos[0]][alice_pos[1]] = "*"
        alice_pos = next_pos
        matrix[alice_pos[0]][alice_pos[1]] = "A"

    else:
        tea = int(matrix[new_row][new_col])
        tea_bags += tea
        matrix[alice_pos[0]][alice_pos[1]] = "*"
        alice_pos = next_pos
        matrix[alice_pos[0]][alice_pos[1]] = "A"
        if tea_bags >= 10:
            matrix[alice_pos[0]][alice_pos[1]] = "*"
            break
if is_party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(' '.join(row)) for row in matrix]
