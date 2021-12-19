size = int(input())
matrix = []

for _ in range(size):
    row = [x for x in input()]
    matrix.append(row)

symbol = input()
found = False
location = []
for row_index in range(size):
    if found:
        break
    for col_index in range(size):
        current_symbol = matrix[row_index][col_index]
        if symbol == current_symbol:
            location = [row_index, col_index]
            found = True

if found:
    print(f"({location[0]}, {location[1]})")
else:
    print(f"{symbol} does not occur in the matrix")
