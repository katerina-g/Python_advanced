def stock_availability(boxes, command, *args):
    if command == "delivery":
        boxes.extend(args)

    elif command == "sell":
        if not args:
            boxes = boxes[1:]

        elif type(args[0]) == int:
            boxes = boxes[args[0]:]

        else:
            for item in args:
                if item in boxes:
                    boxes = [stock for stock in boxes if item != stock]

    return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
