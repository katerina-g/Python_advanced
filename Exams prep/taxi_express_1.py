from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = list(map(int, input().split(', ')))

total_time = 0
while customers and taxis:
    if customers[0] <= taxis[-1]:
        total_time += customers[0]
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()
if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
