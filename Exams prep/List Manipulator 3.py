from collections import deque


def list_manipulator(*args):
    list_nums = deque(args[0])
    command_1 = args[1]
    command_2 = args[2]
    nums = args[3:]
    if command_1 == "add":
        if command_2 == "beginning":
            list_nums.extendleft(reversed(nums))
            return list(list_nums)
        elif command_2 == "end":
            list_nums.extend(nums)
            return list(list_nums)
    elif command_1 == "remove":
        if command_2 == "beginning":
            if len(nums) > 0:
                n = int(nums[0])
                for i in range(0, n):
                    list_nums.popleft()
                return list(list_nums)
            else:
                list_nums.popleft()
                return list(list_nums)
        elif command_2 == "end":
            if len(nums) > 0:
                n = int(nums[0])
                for i in range(n, 0, -1):
                    list_nums.pop()
                return list(list_nums)
            else:
                list_nums.pop()
                return list(list_nums)
print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))




