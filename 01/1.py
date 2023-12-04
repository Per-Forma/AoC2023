
answer = 0
with open('input', 'r') as data:
    for line in data:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        calib_value1 = digits[0]
        calib_value2 = digits[digits.__len__()-1]
        combined_calib_val = calib_value1 + calib_value2
        answer = answer + int(combined_calib_val)
print(answer)
