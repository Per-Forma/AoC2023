import string

answer = 0
symbol_test_list = string.punctuation.replace('.', '')
list_of_answers = []
schema = []

with open('input', 'r') as data:
    for schema_line in data:
        schema.append(schema_line)

for current_line_index, line in enumerate(schema):
    preceding_line_index = current_line_index - 1
    following_line_index = current_line_index + 1
    if preceding_line_index == -1:
        preceding_line = ''
    else:
        preceding_line = schema[preceding_line_index]

    try:
        following_line = schema[following_line_index]
    except IndexError as e:
        following_line = ''

    line_digits = []
    # All list items should be two items long list. 1st item, read_digit, 2nd item start index
    # Represents all digits and their starting index in the line string

    start_digit_index = 0
    operating_char_index = 0
    current_number = ''
    for char_index, char in enumerate(line):
        if operating_char_index is not char_index:
            if char.isdigit():
                current_number = current_number + char
                operating_char_index = operating_char_index + 1
            else:
                line_digit = [current_number, start_digit_index]
                line_digits.append(line_digit)
                current_number = ''
            continue
        if char.isdigit():
            start_digit_index = char_index
            current_number = current_number + char
            operating_char_index = operating_char_index + 2
        else:
            operating_char_index = operating_char_index + 1

    for int_instance in line_digits:
        int_instance_added = False
        preceding_char = line[int_instance[1]-1]
        trailing_char = line[int_instance[1]+len(int_instance[0])]
        if preceding_char in symbol_test_list or trailing_char in symbol_test_list:
            list_of_answers.append(int(int_instance[0]))
            int_instance_added = True
            continue
        adjacent_line_test_range = [int_instance[1]-1, int_instance[1]+len(int_instance[0])+1]
        if adjacent_line_test_range[0] == -1:
            adjacent_line_test_range_upper = adjacent_line_test_range[1]
            adjacent_line_test_range = [0, adjacent_line_test_range_upper]
        preceding_line_test_range = preceding_line[adjacent_line_test_range[0]:adjacent_line_test_range[1]]
        following_line_test_range = following_line[adjacent_line_test_range[0]:adjacent_line_test_range[1]]
        for char in preceding_line_test_range:
            if char in symbol_test_list:
                list_of_answers.append(int(int_instance[0]))
                int_instance_added = True
                break
        if int_instance_added:
            continue
        for char in following_line_test_range:
            if char in symbol_test_list:
                list_of_answers.append(int(int_instance[0]))
                break

answer = sum(list_of_answers)
print(answer)
