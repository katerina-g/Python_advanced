import itertools

rows, cols = [int(el) for el in input().split(', ')]

matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]
total = sum(itertools.chain(*matrix))

print(total)
print(matrix)