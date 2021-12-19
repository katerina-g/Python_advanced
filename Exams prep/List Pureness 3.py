from collections import deque


def best_list_pureness(*args):
    collection = deque(args[0])
    rotations = int(args[1])
    best_pureness = 0
    best_rotation = 0
    for rotation in range(rotations + 1):
        list_pureness = 0
        for idx, val in enumerate(collection):
            list_pureness += idx * val
        if list_pureness > best_pureness:
            best_pureness = list_pureness
            best_rotation = rotation
        collection.rotate()
    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)