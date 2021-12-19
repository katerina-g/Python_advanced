def math_operations(*args, **kwargs):
    nums_list = list(args)
    operation_dict = kwargs
    i = 0
    while nums_list:
        curr_num = nums_list.pop(0)
        if i == 0:
            operation_dict["a"] += curr_num
            i += 1
        elif i == 1:
            operation_dict["s"] -= curr_num
            i += 1
        elif i == 2:
            if curr_num != 0:
                operation_dict["d"] /= curr_num
                i += 1
            else:
                i += 1
                continue
        elif i == 3:
            operation_dict["m"] *= curr_num
            i += 1
        if i == 4:
            i = 0

    return operation_dict


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
