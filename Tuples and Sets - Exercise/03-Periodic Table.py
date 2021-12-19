n = int(input())

unique_chemical_elements = set()
for _ in range(n):
    lines = input().split(' ')
    for el in lines:
        if el not in unique_chemical_elements:
            unique_chemical_elements.add(el)
for element in unique_chemical_elements:
    print(element)