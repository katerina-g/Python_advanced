# def even_nums(nums_list):
#     result = [el for el in nums_list if el % 2 == 0]
#     return result
#
#
# nums = [int(el) for el in input().split(' ')]
# print(even_nums(nums))

nums = [int(el) for el in input().split(' ')]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))