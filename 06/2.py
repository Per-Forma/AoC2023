from numpy import sqrt, prod
from math import ceil, floor

input_data = []
answer = 0
answer_parts = []
race_data = [['', '']]

with open('input') as file:
    for line in file:
        input_data.append(line)

for line_index, line in enumerate(input_data):
    line_contents = line.split()
    if line_contents[0] == 'Time:':
        for e_index, line_element in enumerate(line_contents):
            if line_element == 'Time:':
                continue
            race_data[0][0] = race_data[0][0] + line_element
            # race_data.append([line_element])
    elif line_contents[0] == 'Distance:':
        for index, line_element in enumerate(line_contents):
            if line_element == 'Distance:':
                continue
            race_data[0][1] = race_data[0][1] + line_element
            # race_data[index - 1].append(line_element)

for race in race_data:
    race_record = int(race[1])
    race_ms = int(race[0])
    # equation to find race_distance = (race_ms - charge_ms) * charge_ms
    lower_range = .5 * (race_ms - sqrt(race_ms ** 2 - 4 * race_record))
    if float.is_integer(lower_range):
        lower_range = int(lower_range) + 1
    else:
        lower_range = ceil(lower_range)

    upper_range = .5 * (sqrt(race_ms ** 2 - 4 * race_record) + race_ms)
    if float.is_integer(upper_range):
        upper_range = int(upper_range) - 1
    else:
        upper_range = floor(upper_range)

    answer_parts.append(len(range(lower_range, upper_range+1)))

answer = prod(answer_parts)
print(answer)