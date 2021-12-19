size = int(input())

matrix = []
for _ in range(size):
    row = [int(n) for n in input().split(' ')]
    matrix.append(row)

sum_primary_diagonal = 0

for i in range(size):
    sum_primary_diagonal += matrix[i][i]

print(sum_primary_diagonal)