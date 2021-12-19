from collections import deque

orders = [int(x) for x in input().split(', ')]
employees = [int(x) for x in input().split(', ')]

orders = deque([x for x in orders if 0 < x <= 10])

all_pizza = 0

while orders and employees:
    if orders[0] <= employees[-1]:
        all_pizza += orders[0]
        orders.popleft()
        employees.pop()
    elif orders[0] > employees[-1]:
        orders[0] -= employees[-1]
        all_pizza += employees[-1]
        employees.pop()

if not orders:
    print(f"All orders are successfully completed!\nTotal pizzas made: {all_pizza}\nEmployees: {', '.join([str(x) for x in employees])}")
elif not employees and len(orders) > 0:
    print(f"Not all orders are completed.\nOrders left: {', '.join([str(x) for x in orders])}")

