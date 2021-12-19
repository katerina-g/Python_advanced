import collections


def numbers_searching(*args):
    sorted_args = sorted(args)
    find_nums = []
    for num in range(sorted_args[0], sorted_args[-1] + 1):
        if num not in args:
            find_nums.append(num)
    duplicates = []
    for item, count in collections.Counter(args).items():
        if count > 1:
            duplicates.append(item)
    return [*find_nums, sorted(duplicates)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))