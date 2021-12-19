from collections import deque


bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input(). split()]
symbols = deque(input().split())
honey = 0
total_honey = 0
while bees and nectar:
    first_bee = bees.popleft()
    last_nectar = nectar.pop()
    if last_nectar >= first_bee:
        first_symbol = symbols.popleft()
        if first_symbol == "+":
            honey = first_bee + last_nectar
            total_honey += honey
        elif first_symbol == "-":
            honey = abs(first_bee - last_nectar)
            total_honey += honey
        elif first_symbol == "*":
            honey = first_bee * last_nectar
            total_honey += honey
        elif first_symbol == "/":
            if last_nectar != 0:
                honey = first_bee / last_nectar
                total_honey += honey
    else:
        bees.appendleft(first_bee)
print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")