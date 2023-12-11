answer = 0
asterisk_locations = []  # All items must be two item lists. 1st item line of asterisk, 2nd item column of asterisk
list_of_answers = []
schema = []


def contains_digit(input_string):
    for str_char in input_string:
        if str_char.isdigit():
            return True
        else:
            continue
    return False


def get_prior_char(number_index):
    prior_char = schema[number_index[0]][number_index[1] - 1]
    return prior_char


def get_following_char(number_index):
    following_char = schema[number_index[0]][number_index[1] + 1]
    return following_char


def retrieve_complete_numbers(number_index):
    """number_index must be a vector\nreturns a complete number as list of digits"""
    returned_numbers = []
    digit_in_question = schema[number_index[0]][number_index[1]]
    if not contains_digit(digit_in_question):
        return Exception
    returned_numbers.append(digit_in_question)
    prior_char = get_prior_char(number_index)
    if prior_char.isdigit():
        number_index = [number_index[0], number_index[1] - 1]
        while prior_char.isdigit():
            returned_numbers.append(prior_char)
            prior_char = get_prior_char(number_index)
            number_index = [number_index[0], number_index[1] - 1]
        return returned_numbers
    following_char = get_following_char(number_index)
    if following_char.isdigit():
        number_index = [number_index[0], number_index[1] + 1]
        while following_char.isdigit():
            returned_numbers.append(following_char)
            following_char = get_following_char(number_index)
            number_index = [number_index[0], number_index[1] + 1]
        return returned_numbers
    return returned_numbers


with open('input', 'r') as data:
    for schema_line in data:
        schema.append(schema_line)

for line_index, line in enumerate(schema):
    for char_index, char in enumerate(line):
        if char == '*':
            asterisk_locations.append([line_index, char_index])

for asterisk_location in asterisk_locations:
    adjacent_numbers = []
    preceding_char = schema[asterisk_location[0]][asterisk_location[1] - 1]
    trailing_char = schema[asterisk_location[0]][asterisk_location[1] + 1]
    upper_adjacent_chars = schema[asterisk_location[0] - 1][asterisk_location[1] - 1:asterisk_location[1] + 2]
    lower_adjacent_chars = schema[asterisk_location[0] + 1][asterisk_location[1] - 1:asterisk_location[1] + 2]
    preceding_char_is_digit = contains_digit(preceding_char)
    trailing_char_is_digit = contains_digit(trailing_char)
    upper_adjacent_chars_contain_digit = contains_digit(upper_adjacent_chars)
    lower_adjacent_chars_contain_digit = contains_digit(lower_adjacent_chars)
    if preceding_char_is_digit:
        preceding_number = retrieve_complete_numbers([asterisk_location[0], asterisk_location[1] - 1])
        preceding_number.reverse()
        collapsed_int_str = ''
        for digit in preceding_number:
            collapsed_int_str = collapsed_int_str + digit
        collapsed_int = int(collapsed_int_str)
        adjacent_numbers.append(collapsed_int)
    if trailing_char_is_digit:
        trailing_number = retrieve_complete_numbers([asterisk_location[0], asterisk_location[1] + 1])
        collapsed_int_str = ''
        for digit in trailing_number:
            collapsed_int_str = collapsed_int_str + digit
        collapsed_int = int(collapsed_int_str)
        adjacent_numbers.append(collapsed_int)
    complete_upper_digit_string = upper_adjacent_chars

    if upper_adjacent_chars_contain_digit:
        # find full range of digits following upper_adjacent_chars
        if upper_adjacent_chars[2].isdigit():
            following_char_index = [asterisk_location[0] - 1, asterisk_location[1] + 1]
            following_char = get_following_char(following_char_index)
            while following_char.isdigit():
                complete_upper_digit_string = complete_upper_digit_string + following_char
                following_char_index = [following_char_index[0], following_char_index[1] + 1]
                following_char = get_following_char(following_char_index)
        if upper_adjacent_chars[0].isdigit():
            preceding_char_index = [asterisk_location[0] - 1, asterisk_location[1] - 1]
            preceding_char = get_prior_char(preceding_char_index)
            while preceding_char.isdigit():
                complete_upper_digit_string = preceding_char + complete_upper_digit_string
                preceding_char_index = [preceding_char_index[0], preceding_char_index[1] - 1]
                preceding_char = get_prior_char(preceding_char_index)
    # extract discrete digits from complete_upper_digit_string
    discrete_digit_string = ''
    for char in complete_upper_digit_string:
        if not char.isdigit():
            if discrete_digit_string.isdigit():
                adjacent_numbers.append(int(discrete_digit_string))
                discrete_digit_string = ''
                continue
            continue
        discrete_digit_string = discrete_digit_string + char
    if discrete_digit_string.isdigit():
        adjacent_numbers.append(int(discrete_digit_string))

    complete_lower_digit_string = lower_adjacent_chars
    if lower_adjacent_chars_contain_digit:
        if lower_adjacent_chars[2].isdigit():
            following_char_index = [asterisk_location[0] + 1, asterisk_location[1] + 1]
            following_char = get_following_char(following_char_index)
            while following_char.isdigit():
                complete_lower_digit_string = complete_lower_digit_string + following_char
                following_char_index = [following_char_index[0], following_char_index[1] + 1]
                following_char = get_following_char(following_char_index)
        if lower_adjacent_chars[0].isdigit():
            preceding_char_index = [asterisk_location[0] + 1, asterisk_location[1] - 1]
            preceding_char = get_prior_char(preceding_char_index)
            while preceding_char.isdigit():
                complete_lower_digit_string = preceding_char + complete_lower_digit_string
                preceding_char_index = [preceding_char_index[0], preceding_char_index[1] - 1]
                preceding_char = get_prior_char(preceding_char_index)

        # extract discrete digits from complete_lower_digit_string
        discrete_digit_string = ''
        for char in complete_lower_digit_string:
            if not char.isdigit():
                if discrete_digit_string.isdigit():
                    adjacent_numbers.append(int(discrete_digit_string))
                    discrete_digit_string = ''
                    continue
                continue
            discrete_digit_string = discrete_digit_string + char
        if discrete_digit_string.isdigit():
            adjacent_numbers.append(int(discrete_digit_string))

    if len(adjacent_numbers) == 2:
        gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
        list_of_answers.append(gear_ratio)

answer = sum(list_of_answers)
print(answer)
