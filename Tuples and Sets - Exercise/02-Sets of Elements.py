line = input().split(' ')
n = int(line[0])
m = int(line[1])


length_n_numbers = set()
length_m_numbers = set()
for _ in range(n):
    number = int(input())
    length_n_numbers.add(number)
for _ in range(m):
    number = int(input())
    length_m_numbers.add(number)

repeating_numbers = length_n_numbers.intersection(length_m_numbers)

for num in repeating_numbers:
    print(num)
