answer = 0
string_start = 'Game '
string_end = ':'

with open('input', 'r') as data:
    for game_line in data:
        start_index = game_line.index(string_start) + len(string_start)
        end_index = game_line.index(string_end)
        game_id = game_line[start_index:end_index]

        # Strip Game information from beginning of string
        game_line = game_line[end_index + 1:].strip()

        max_red = 0
        max_green = 0
        max_blue = 0

        # Separate rounds
        game_rounds = (game_line.split(';'))
        game_rounds_new = []
        for game in game_rounds:
            game_rounds_new.append(game.strip())
        game_rounds = game_rounds_new
        for game_round in game_rounds:

            round_list = game_round.split(',')
            for color_cube in round_list:
                count_color = color_cube.split()
                count = int(count_color[0])
                color = count_color[1]
                if color == 'red':
                    if count > max_red:
                        max_red = count
                if color == 'green':
                    if count > max_green:
                        max_green = count
                if color == 'blue':
                    if count > max_blue:
                        max_blue = count

        powerof = max_red * max_green * max_blue
        answer = answer + powerof
    print(answer)
