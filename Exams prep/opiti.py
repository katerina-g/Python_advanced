rows, cols = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())


line = input()
while not line == "END":
    split_line = line.split()
    command = split_line[0]
    if command != "swap" and len(split_line) != 5:
        print("Invalid input!")
    else:
        row_1 = int(split_line[1])
        col_1 = int(split_line[2])
        row_2 = int(split_line[3])
        col_2 = int(split_line[4])
        if (row_1 and row_2) in range(rows) and (col_1 and col_2) in range(cols):
            temp = matrix[row_1][col_1]
            matrix[row_1][col_1] = matrix[row_2][col_2]
            matrix[row_2][col_2] = temp
            [print(*r, sep=' ') for r in matrix]
        else:
            print("Invalid input!")

    line = input()
