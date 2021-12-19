from collections import deque


def stock_availability(inventory_list, command, *args):
    inventory_list = deque(inventory_list)
    if command == "delivery":
        inventory_list.extend(args)
    elif command == "sell":
        if len(args) == 0:
            inventory_list.popleft()
        else:
            args = [str(el) for el in args]
            if args[0].isdigit():
                n = int(args[0])
                for i in range(n):
                    inventory_list.popleft()
            else:
                while args[0] in inventory_list:
                    inventory_list.remove(args[0])
    return list(inventory_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
