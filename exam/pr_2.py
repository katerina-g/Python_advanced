def is_valid(r, c, s):
    if 0 <= r < s and 0 <= c < s:
        return True
    return False


matrix = []
n = 7
pl_1_sc = 501
pl_2_sc = 501
pl_1_t = 0
pl_2_t = 0
throws = 0

pl_1, pl_2 = input().split(", ")
for row in range(n):
    line = input().split()
    matrix.append(line)

while True:
    positions = input().strip("()")
    row_index, col_index = positions.split(", ")
    row_index = int(row_index)
    col_index = int(col_index)
    throws += 1
    if throws % 2 != 0:
        pl_1_t += 1
        if is_valid(row_index, col_index, n):
            if matrix[row_index][col_index] == "B":
                print(f"{pl_1} won the game with {pl_1_t} throws!")
                break
            elif matrix[row_index][col_index] == "D":
                pl_1_sc -= (int(matrix[row_index][0]) + int(matrix[row_index][6]) + int(matrix[0][col_index]) + int(matrix[6][col_index])) * 2
            elif matrix[row_index][col_index] == "T":
                pl_1_sc -= (int(matrix[row_index][0]) + int(matrix[row_index][6]) + int(matrix[0][col_index]) + int(matrix[6][col_index])) * 3
            else:
                pl_1_sc -= int(matrix[row_index][col_index])
            if pl_1_sc <= 0:
                print(f"{pl_1} won the game with {pl_1_t} throws!")
                break
    else:
        pl_2_t += 1
        if is_valid(row_index, col_index, n):
            if matrix[row_index][col_index] == "B":
                print(f"{pl_2} won the game with {pl_2_t} throws!")
                break
            elif matrix[row_index][col_index] == "D":
                pl_2_sc -= (int(matrix[row_index][0]) + int(matrix[row_index][6]) + int(matrix[0][col_index]) + int(
                    matrix[6][col_index])) * 2
            elif matrix[row_index][col_index] == "T":
                pl_2_sc -= (int(matrix[row_index][0]) + int(matrix[row_index][6]) + int(matrix[0][col_index]) + int(
                    matrix[6][col_index])) * 3
            else:
                pl_2_sc -= int(matrix[row_index][col_index])
            if pl_2_sc <= 0:
                print(f"{pl_2} won the game with {pl_2_t} throws!")
                break






