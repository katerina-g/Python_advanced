def read_matrix():
    rows_count = int(input())
    return [[int(x) for x in input().split(', ')] for _ in range(rows_count)]


matrix = read_matrix()

print([x for row in matrix for x in row])