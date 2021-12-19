n = int(input())

intersections = []
for _ in range(n):
    data = input().split('-')
    first_range = data[0]
    second_range = data[1]

    start_1, stop_1 = [int(el) for el in first_range.split(',')]
    first_seq = range(start_1, stop_1 + 1)
    start_2, stop_2 = [int(el) for el in second_range.split(',')]
    second_seq = range(start_2, stop_2 + 1)
    intersection = set(first_seq).intersection(second_seq)
    intersections.append(intersection)


longest = sorted(intersections, key=lambda x: -len(x))[0]
print(f"Longest intersection is {list(longest)} with length {len(longest)}")