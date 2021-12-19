def odd_sum_nums(nums):
    odd_sum = sum(filter(lambda x: x % 2 == 1, nums))
    return odd_sum * len(nums)


def even_sum_nums(nums):
    even_sum = sum(filter(lambda x: x % 2 == 0, nums))
    return even_sum * len(nums)


command = input()
numbers = [int(el) for el in input().split(' ')]
if command == "Odd":
    print(odd_sum_nums(numbers))
else:
    print(even_sum_nums(numbers))