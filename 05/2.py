from collections import OrderedDict
answer = 0
input_data = []
section_index = {}
section_index_list = []
seeds = []
seeds_ranges = []
locations = []
s2s_maps = []
s2f_maps = []
f2w_maps = []
w2l_maps = []
l2t_maps = []
t2h_maps = []
h2l_maps = []
s2s_map_dict = {}
s2f_map_dict = {}
f2w_map_dict = {}
w2l_map_dict = {}
l2t_map_dict = {}
t2h_map_dict = {}
h2l_map_dict = {}
s_strings = []
s2s_strings = []
s2f_strings = []
f2w_strings = []
w2l_strings = []
l2t_strings = []
t2h_strings = []
h2l_strings = []


def input_to_output_range_calculation(input_int, ranges_for_compare):
    return_val = input_int
    if input_int in ranges_for_compare[0]:
        input_range_index = input_int - ranges_for_compare[0][0]
        return_val = input_range_index + ranges_for_compare[1][0]
    return return_val


def calculate_location_from_seed(seed_value):
    """seed_value must be an integer"""
    location_value = seed_value
    return location_value


def create_mapping_dict(mapping_list):
    source_start = int(mapping_list[1])
    source_end = int(mapping_list[1]) + int(mapping_list[2])
    destination_start = int(mapping_list[0])
    destination_end = int(mapping_list[0]) + int(mapping_list[2])
    source_range = range(source_start, source_end)
    destination_range = range(destination_start, destination_end)
    return [source_range, destination_range]


with open('input') as file:
    for line in file:
        input_data.append(line)

# Locate starting line numbers for sections from input data
for line_number, input_line in enumerate(input_data):
    if input_line.startswith('seeds:'):
        section_index['s'] = line_number
    elif input_line.startswith('seed-to-soil map'):
        section_index['s2s'] = line_number
    elif input_line.startswith('soil-to-fertilizer map'):
        section_index['s2f'] = line_number
    elif input_line.startswith('fertilizer-to-water map'):
        section_index['f2w'] = line_number
    elif input_line.startswith('water-to-light map'):
        section_index['w2l'] = line_number
    elif input_line.startswith('light-to-temperature map'):
        section_index['l2t'] = line_number
    elif input_line.startswith('temperature-to-humidity map'):
        section_index['t2h'] = line_number
    elif input_line.startswith('humidity-to-location map'):
        section_index['h2l'] = line_number

section_index_sorted = OrderedDict(sorted(section_index.items(), key=lambda item: item[1]))

for item in section_index_sorted.items():
    section_index_list.append(item)

section_index_length = len(section_index_sorted) - 1


for item_index, item in enumerate(section_index_list):
    item_start_line = item[1]
    try:
        item_end_line = section_index_list[item_index + 1][1] - 1
    except IndexError:
        item_end_line = len(input_data)

    if item[0] == 's':
        s_strings = input_data[item_start_line:item_end_line]
    elif item[0] == 's2s':
        s2s_strings = input_data[item_start_line:item_end_line]
    elif item[0] == 's2f':
        s2f_strings = input_data[item_start_line:item_end_line]
    elif item[0] == 'f2w':
        f2w_strings = input_data[item_start_line:item_end_line]
    elif item[0] == 'w2l':
        w2l_strings = input_data[item_start_line:item_end_line]
    elif item[0] == 'l2t':
        l2t_strings = input_data[item_start_line:item_end_line]
    elif item[0] == 't2h':
        t2h_strings = input_data[item_start_line:item_end_line]
    elif item[0] == 'h2l':
        h2l_strings = input_data[item_start_line:item_end_line]

for line in s_strings:
    line = line.strip()
    line = line[7:]
    seeds = line.split()
for line in s2s_strings:
    if line[0:5] == 'seed-':
        continue
    line = line.strip()
    line = line.split()
    s2s_maps.append(line)
for line in s2f_strings:
    if line[0:5] == 'soil-':
        continue
    line = line.strip()
    line = line.split()
    s2f_maps.append(line)
for line in f2w_strings:
    if line[0:5] == 'ferti':
        continue
    line = line.strip()
    line = line.split()
    f2w_maps.append(line)
for line in w2l_strings:
    if line[0:5] == 'water':
        continue
    line = line.strip()
    line = line.split()
    w2l_maps.append(line)
for line in l2t_strings:
    if line[0:5] == 'light':
        continue
    line = line.strip()
    line = line.split()
    l2t_maps.append(line)
for line in t2h_strings:
    if line[0:5] == 'tempe':
        continue
    line = line.strip()
    line = line.split()
    t2h_maps.append(line)
for line in h2l_strings:
    if line[0:5] == 'humid':
        continue
    line = line.strip()
    line = line.split()
    h2l_maps.append(line)

for seed_index, seed in enumerate(seeds):
    if seed_index % 2 == 0:
        seed_start = int(seed)
        seed_range_len = int(seeds[seed_index + 1])
        seeds_ranges.append(range(seed_start, seed_start + seed_range_len))
    continue
    # seeds[seed] = int(seeds[seed])

maps_dict = {}
maps_dict['s2s_maps'] = s2s_maps
maps_dict['s2f_maps'] = s2f_maps
maps_dict['f2w_maps'] = f2w_maps
maps_dict['w2l_maps'] = w2l_maps
maps_dict['l2t_maps'] = l2t_maps
maps_dict['t2h_maps'] = t2h_maps
maps_dict['h2l_maps'] = h2l_maps


for mappings in maps_dict.items():
    mapping_section = mappings[0]
    for mapp in mappings[1]:
        mapping_obj = create_mapping_dict(mapp)
        if mapping_section == 's2s_maps':
            s2s_map_dict[mapping_obj[0]] = mapping_obj[1]
        elif mapping_section == 's2f_maps':
            s2f_map_dict[mapping_obj[0]] = mapping_obj[1]
        elif mapping_section == 'f2w_maps':
            f2w_map_dict[mapping_obj[0]] = mapping_obj[1]
        elif mapping_section == 'w2l_maps':
            w2l_map_dict[mapping_obj[0]] = mapping_obj[1]
        elif mapping_section == 'l2t_maps':
            l2t_map_dict[mapping_obj[0]] = mapping_obj[1]
        elif mapping_section == 't2h_maps':
            t2h_map_dict[mapping_obj[0]] = mapping_obj[1]
        elif mapping_section == 'h2l_maps':
            h2l_map_dict[mapping_obj[0]] = mapping_obj[1]

for seed in seeds:
    for range_item in s2s_map_dict.items():
        soil_number = input_to_output_range_calculation(seed,range_item)
        if not soil_number == seed:
            break
    for range_item in s2f_map_dict.items():
        fertilizer_number = input_to_output_range_calculation(soil_number, range_item)
        if not fertilizer_number == soil_number:
            break
    for range_item in f2w_map_dict.items():
        water_number = input_to_output_range_calculation(fertilizer_number, range_item)
        if not water_number == fertilizer_number:
            break
    for range_item in w2l_map_dict.items():
        light_number = input_to_output_range_calculation(water_number, range_item)
        if not light_number == water_number:
            break
    for range_item in l2t_map_dict.items():
        temp_number = input_to_output_range_calculation(light_number, range_item)
        if not temp_number == light_number:
            break
    for range_item in t2h_map_dict.items():
        humidity_number = input_to_output_range_calculation(temp_number, range_item)
        if not humidity_number == temp_number:
            break
    for range_item in h2l_map_dict.items():
        location_number = input_to_output_range_calculation(humidity_number, range_item)
        if not location_number == humidity_number:
            break

    locations.append(location_number)

answer = min(locations)
print(answer)
