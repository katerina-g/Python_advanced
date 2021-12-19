n = int(input())

odd_numbers = set()
even_numbers = set()
for i in range(1, n + 1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // i
    if current_sum % 2 == 0:
        even_numbers.add(current_sum)
    else:
        odd_numbers.add(current_sum)
odd_sum = sum(odd_numbers)
even_sum = sum(even_numbers)
if odd_sum == even_sum:
    modified_set = [str(el) for el in odd_numbers.union(even_numbers)]
    print(', '.join(modified_set))
elif odd_sum > even_sum:
    modified_set = [str(el) for el in odd_numbers.difference(even_numbers)]
    print(', '.join(modified_set))
else:
    modified_set = [str(el) for el in odd_numbers.symmetric_difference(even_numbers)]
    print(', '.join(modified_set))