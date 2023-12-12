answer = 0
ticket_data = []
ticket_dict = {}

with open('input', 'r') as data:
    for line in data:
        ticket_data.append(line)

for card in ticket_data:
    card_id_game_split = card.split(':')
    card_id_str = card_id_game_split[0]
    card_id = card_id_str.split(' ')[1]
    card_game_data = card_id_game_split[1].split('|')
    card_our_digits_str = card_game_data[1].strip()
    card_winning_digits_str = card_game_data[0].strip()
    our_digits_list = card_our_digits_str.split()
    winning_digits_list = card_winning_digits_str.split()

    matching_digits = []
    for my_digit in our_digits_list:
        if my_digit in winning_digits_list:
            matching_digits.append(my_digit)

    card_score = 0
    for digit in matching_digits:
        if card_score == 0:
            card_score = 1
        else:
            card_score = card_score * 2

    answer = answer + card_score

    if len(matching_digits) > 10:
        print('possible error in ' + card_id_str)

print(answer)
