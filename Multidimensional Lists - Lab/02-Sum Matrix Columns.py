rows, cols = [int(el) for el in input().split(', ')]

matrix = []
for _ in range(rows):
    row = [int(n) for n in input().split(' ')]
    matrix.append(row)

result = []

for column_index in range(cols):
    column_sum = 0
    for row_index in range(rows):
        column_sum += matrix[row_index][column_index]
    result.append(column_sum)
[print(x) for x in result]