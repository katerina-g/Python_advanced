def read_matrix():
    matrix = [[x for x in input().split(" ")] for n in range(7)]
    return matrix


def is_valid(r, c, size):
    return 0 <= r < size and 0 <= c < size


player_1_score = 501
player_2_score = 501
player_1, player_2 = input().split(", ")
turns_counter = 1
turns_counter_player_1 = 0
turns_counter_player_2 = 0

matrix = read_matrix()

while True:
    row, col = input().split(", ")
    row, col = int(row[1:]), int(col[:-1])
    turns_counter += 1

    if turns_counter % 2 == 0:
        turns_counter_player_1 += 1
        if is_valid(row, col, size=7):
            if matrix[row][col].isdigit():
                player_1_score -= int(matrix[row][col])
            elif matrix[row][col] == "D":
                player_1_score -= ((int(matrix[row][0])) + (int(matrix[row][6])) + (int(matrix[0][col])) + (
                    int(matrix[6][col]))) * 2
            elif matrix[row][col] == "T":
                player_1_score -= ((int(matrix[row][0])) + (int(matrix[row][6])) + (int(matrix[0][col])) + (
                    int(matrix[6][col]))) * 3
            elif matrix[row][col] == "B":
                print(f"{player_1} won the game with {turns_counter_player_1} throws!")
                break
            if player_1_score <= 0:
                print(f"{player_1} won the game with {turns_counter_player_1} throws!")
                break

    else:
        turns_counter_player_2 += 1
        if is_valid(row, col, size=7):
            if matrix[row][col].isdigit():
                player_2_score -= int(matrix[row][col])
            elif matrix[row][col] == "D":
                player_2_score -= ((int(matrix[row][0])) + (int(matrix[row][6])) + (int(matrix[0][col])) + (
                    int(matrix[6][col]))) * 2
            elif matrix[row][col] == "T":
                player_2_score -= ((int(matrix[row][0])) + (int(matrix[row][6])) + (int(matrix[0][col])) + (
                    int(matrix[6][col]))) * 3
            elif matrix[row][col] == "B":
                print(f"{player_2} won the game with {turns_counter_player_2} throws!")
                break
            if player_2_score <= 0:
                print(f"{player_2} won the game with {turns_counter_player_2} throws!")
                break

