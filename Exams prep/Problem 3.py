# def get_magic_triangle(n):
#     triangle = []
#     prev_row = []
#     for i in range(1, n + 1):
#         row = [0 < j < i - 1 and i > 2 and prev_row[j - 1] + prev_row[j] or 1 for j in range(0, i)]
#         prev_row = row
#         triangle += [row]
#     print(triangle)
#
#
# get_magic_triangle(5)

# def pascals_triangle(rows):
#     answer = []
#     triangle = []
#     for row in range(rows):
#         answer.append(1)  # both widen the row and initialize last element
#         triangle.append(answer)
#         for i in range(row - 1, 0, -1):  # fill in the row, right to left
#             answer[i] += answer[i - 1]  # current computed from previous
#
#         print(answer)
#
# pascals_triangle(5)
# def combination(n, k):
#     if k == 0 or k == n:
#         return 1
#     return combination(n - 1, k - 1) + combination(n - 1, k)
#
# def pascals_triangle(rows):
#     for row in range(rows):
#         answer = []
#         for column in range(row + 1):
#             answer.append((combination(row, column)))
#         print(answer)
#
# pascals_triangle(5)
def get_magic_triangle(n, triangle=[[1]]):
    if n > len(triangle):
        last_row = triangle[-1]
        next_row = [a+b for (a, b) in zip([0] + last_row, last_row + [0])]
        return get_magic_triangle(n, triangle + [next_row])
    return triangle

get_magic_triangle(5)