answer = 0
red_cubes = 12
green_cubes = 13
blue_cubes = 14
with open('input', 'r') as data:
    for gameline in data:
        string_start = 'Game '
        string_end = ':'
        start_index = gameline.index(string_start)+len(string_start)
        end_index = gameline.index(string_end)
        game_id = gameline[start_index:end_index]

        # Strip Game information from beginning of string
        gameline = gameline[end_index+1:]
        # gameline.find(':')
        # Beginning with a True assumption for round validity. We will prove the existence of a bad
        # round rather than its absence
        valid_round = True
        # Separate rounds
        gamerounds = gameline.split(';')
        # Detect false round
        for round in gamerounds:

            cubes = round.split(',')
            for cube in cubes:
                count_color = cube.split()
                count = int(count_color[0])
                color = count_color[1]
                if color == 'red':
                    if count > red_cubes:
                        valid_round = False
                if color == 'green':
                    if count > green_cubes:
                        valid_round = False
                if color == 'blue':
                    if count > blue_cubes:
                        valid_round = False

        if valid_round:
            answer = answer + int(game_id)

    print(answer)
