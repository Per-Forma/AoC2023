
answer = 0
spelled_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
max_length_of_digit_spelling = 5
with open('input', 'r') as data:
    for line in data:
        # line = 'jhctmxconelfkgmprnfourseven8twofkjvlvnjgd'
        ending_spelled_digit = None
        beginning_spelled_digit = None
        spelled_digits_in_beginning = []
        spelled_digits_in_ending = []
        ending_spelled_index = 0
        beginning_spelled_index = 1000

        ending_spelled_digits_list = []
        beginning_spelled_digits_list = []
        line = line.lower()
        digits = []
        position_of_digits = []
        for pos, char in enumerate(line):
            if char.isdigit():
                position_of_digits.append(pos)
                digits.append(char)
        if len(position_of_digits) > 0:
            beginning = line[0:position_of_digits[0]]
        else:
            beginning = line

        if len(position_of_digits) > 0:
            ending = line[position_of_digits[-1]+1:]
        else:
            ending = line

        for spelled in spelled_digits:
            if spelled in beginning:
                spelled_digits_in_beginning.append(spelled)
            if spelled in ending:
                spelled_digits_in_ending.append(spelled)

        if spelled_digits_in_beginning.__len__() == 0:
            calib_value1 = digits[0]
        else:
            for item in spelled_digits_in_beginning:
                index_of_item = beginning.index(item)
                if index_of_item <= beginning_spelled_index:
                    beginning_spelled_index = index_of_item
                    calib_value1 = spelled_digits.index(item) + 1

        if spelled_digits_in_ending.__len__() == 0:
            calib_value2 = digits[digits.__len__() - 1]
        else:
            for item in spelled_digits_in_ending:
                index_of_item = ending.index(item)
                if index_of_item >= ending_spelled_index:
                    ending_spelled_index = index_of_item
                    calib_value2 = spelled_digits.index(item) + 1

        combined_calib_val = str(calib_value1) + str(calib_value2)
        print(combined_calib_val + ' ' + line)
        answer = answer + int(combined_calib_val)
print(answer)
