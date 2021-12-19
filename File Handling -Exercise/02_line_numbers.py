import re

letter_pattern = r"[A-Za-z]"
punctuation_marks_pattern = r"[-,.!?']"


def write_result(res):
    with open("output.txt", "a") as file:
        file.writelines(res)


def get_sum_marks(line, pattern):
    return len(re.findall(pattern, line))


with open("text.txt", "r") as file:
    lines = file.readlines()
    counter = 1
    for line in lines:
        letters_count = get_sum_marks(line, letter_pattern)
        punctuations_count = get_sum_marks(line, punctuation_marks_pattern)
        write_result(f"Line {counter}: {line[:-1]} ({letters_count})({punctuations_count})\n")
        counter += 1

