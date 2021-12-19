import re

PUNCTUATION_MARKS = r"[\-\?\!\,\.']"
LETTERS_PATTERN = r'[a-z]'


def count_matches(line, pattern):
    return len(re.findall(pattern, line, re.IGNORECASE))


def generate_output_file(input_path):
    with open(input_path, 'r') as input_f, open('output.txt', 'w') as output_f:
        for line_num, line in enumerate(input_f, 1):
            stripped_line = line.rstrip()
            letters_count = count_matches(line, LETTERS_PATTERN)
            punctuation_count = count_matches(line, PUNCTUATION_MARKS)

            new_line = f'Line {line_num}: {stripped_line} ({letters_count})({punctuation_count})\n'
            output_f.write(new_line)


input_file = 'text.txt'
generate_output_file(input_file)
