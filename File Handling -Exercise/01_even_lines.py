import re


def replace_special_symbols(line):
    return re.sub(r"[-,.!?]", "@", line)


with open("text.txt", "r") as file:
    lines = file.readlines()
    for row_num in range(len(lines)):
        if row_num % 2 == 0:
            symbol_replaced = replace_special_symbols(lines[row_num]).split()
            print(" ".join(symbol_replaced[::-1]))
