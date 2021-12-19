n = int(input())

numbers = []

for _ in range(n):
    data = input().split(' ')
    command = int(data[0])
    if command == 1:
        numbers.append(int(data[1]))
    elif command == 2:
        if numbers:
            numbers.pop()
    elif command == 3:
        if numbers:
            print(max(numbers))
    elif command == 4:
        if numbers:
            print(min(numbers))

print(', '.join([str(x) for x in reversed(numbers)]))