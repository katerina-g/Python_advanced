rows, cols = [int(el) for el in input().split(' ')]

matrix = []

for _ in range(rows):
    matrix.append(input().split(' '))

data = input()

while not data == "END":
    split_data = data.split(' ')
    command = split_data[0]
    if command == "swap" and len(split_data) == 5:
        current_row = int(split_data[1])
        current_col = int(split_data[2])
        row_to_swap = int(split_data[3])
        col_to_swap = int(split_data[4])
        if (current_row and row_to_swap) in range(rows) and (current_col and col_to_swap) in range(cols):
            matrix[current_row][current_col], matrix[row_to_swap][col_to_swap] = matrix[row_to_swap][col_to_swap], matrix[current_row][current_col]
            [print(*r, sep=' ')for r in matrix]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    data = input()
