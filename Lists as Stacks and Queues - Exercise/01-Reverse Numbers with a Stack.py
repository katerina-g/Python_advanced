def reverse_numbers(numbers):
    st = []
    for num in numbers:
        st.append(num)
    reversed_numbers = []
    while st:
        num = st.pop()
        reversed_numbers.append(num)
    return ' '.join(reversed_numbers)


print(reverse_numbers(input().split(' ')))
