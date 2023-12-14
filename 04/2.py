import copy
answer = 0
ticket_data = []
ticket_dict = {}
won_ticket_dict = {}
working_ticket_data = []
card_id = 0


def process_tickets(tickets):
    """'tickets' must be a dictionary"""
    global unprocessed_tickets
    global won_ticket_dict
    global key
    for this_ticket_id in tickets:
        this_ticket = copy.deepcopy(unprocessed_tickets.get(this_ticket_id))
        this_ticket['processed'] = True
        won_ticket_dict[this_ticket_id] = this_ticket
        del unprocessed_tickets[this_ticket_id]
        if len(this_ticket.get('matching_digits')) > 0:
            for match_digit_index, digit in enumerate(this_ticket.get('matching_digits')):
                match_digit_count = match_digit_index + 1
                key += 1
                new_copied_ticket = copy.deepcopy(ticket_dict.get(int(this_ticket.get('card_id')) + match_digit_count))
                unprocessed_tickets[key] = new_copied_ticket


with open('input', 'r') as data:
    for line in data:
        ticket_data.append(line)

for ticket_index, card in enumerate(ticket_data):
    card_id_game_split = card.split(':')
    card_id_str = card_id_game_split[0]
    card_id = card_id_str.split()[1]
    card_game_data = card_id_game_split[1].split('|')
    card_our_digits_str = card_game_data[1].strip()
    card_winning_digits_str = card_game_data[0].strip()
    our_digits_list = card_our_digits_str.split()
    winning_digits_list = card_winning_digits_str.split()

    matching_digits = []
    for my_digit in our_digits_list:
        if my_digit in winning_digits_list:
            matching_digits.append(my_digit)

        ticket_dict[int(card_id)] = {'card_id': card_id, 'our_digits': our_digits_list,
                                     'winning_digits': winning_digits_list, 'processed': False,
                                     'matching_digits': matching_digits}

key = int(card_id)
unprocessed_tickets = copy.deepcopy(ticket_dict)

while len(unprocessed_tickets) > 0:
    tickets_for_func = copy.deepcopy(unprocessed_tickets)
    process_tickets(tickets_for_func)

answer = len(won_ticket_dict)

print(str(answer))
