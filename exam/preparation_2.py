matrix = []
player_pos = []
target_count = 0
target_hit = []
directions = {"up": [-1, 0],
              "down": [+1, 0],
              "left": [0, -1],
              "right": [0, +1]
              }

for row in range(5):
    line = input().split()
    for col in range(5):
        if line[col] == "A":
            player_pos = row, col
        elif line[col] == "x":
            target_count += 1

    matrix.append(line)


commands_count = int(input())

for _ in range(commands_count):
    commands = input(). split()
    direction = commands[1]
    move = directions[direction]
    if commands[0] == "shoot":
        shoot_pos = [player_pos[0] + move[0], player_pos[1] + move[1]]
        while 0 <= shoot_pos[0] < 5 and 0 <= shoot_pos[1] < 5:
            if matrix[shoot_pos[0]][shoot_pos[1]] == "x":
                target_count -= 1
                target_hit.append([shoot_pos[0], shoot_pos[1]])
                matrix[shoot_pos[0]][shoot_pos[1]] = "."
                if target_count == 0:
                    print(f"Training completed! All {len(target_hit)} targets hit.")
                    break
            shoot_pos[0] += move[0]
            shoot_pos[1] += move[1]

    elif commands[0] == "move":
        steps = int(commands[2])
        next_pos = [move[0] * steps, move[1] * steps]
        new_pl_p = [player_pos[0] + next_pos[0], player_pos[1] + next_pos[1]]
        if 0 <= new_pl_p[0] < 5 and 0 <= new_pl_p[1] < 5 and matrix[new_pl_p[0]][new_pl_p[1]] == ".":
            matrix[player_pos[0]][player_pos[1]] = "."
            player_pos = new_pl_p
            matrix[player_pos[0]][player_pos[1]] = "A"
if target_count > 0:
    print(f"Training not completed! {target_count} targets left.")

for el in target_hit:
    print(el)




