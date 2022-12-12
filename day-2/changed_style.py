score = 0
alpha_mapping = {'AX': 3, 'BX': 1, 'CX': 2,
                 'AY': 4, 'BY': 5, 'CY': 6,
                 'AZ': 8, 'BZ': 9, 'CZ': 7}

with open('input.txt', 'r') as puzzle_input:
    games = puzzle_input.readlines()
    for game in games:
        game = game.replace('\n', '')
        combination = game.replace(' ', '')
        score += alpha_mapping[combination]

print(score)
