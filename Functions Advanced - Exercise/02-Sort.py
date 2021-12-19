def sorted_nums(nums):
    result = sorted([el for el in nums])
    return result


nums = [int(el) for el in input().split(' ')]
print(sorted_nums(nums))