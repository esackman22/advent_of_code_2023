import re

# Part I
bag = {'red': 12, 'green': 13, 'blue': 14}
total = 0
with open('day_2_input.csv') as f:
    for game in f:
        game_id = int(re.search('Game (\d+)', game)[1])
        reds = re.findall("(\d+) red", game)
        greens = re.findall("(\d+) green", game)
        blues = re.findall("(\d+) blue", game)
        is_valid = True

        for red in reds:
            if int(red) > bag['red']:
                is_valid = False

        for green in greens:
            if int(green) > bag['green']:
                is_valid = False

        for blue in blues:
            if int(blue) > bag['blue']:
                is_valid = False

        if is_valid:
            total += game_id

print(total)

# Part II
powers_sum = 0
with open('day_2_input.csv') as f:
    for game in f:
        reds = re.findall("(\d+) red", game)
        greens = re.findall("(\d+) green", game)
        blues = re.findall("(\d+) blue", game)

        max_red = -1
        max_green = -1
        max_blue = -1

        for red in reds:
            max_red = max(max_red, int(red))

        for green in greens:
            max_green = max(max_green, int(green))

        for blue in blues:
            max_blue = max(max_blue, int(blue))

        powers_sum += max_red * max_green * max_blue

print(powers_sum)