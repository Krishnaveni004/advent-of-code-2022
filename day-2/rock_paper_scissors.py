score = 0
alpha_mapping = {'AX': 4, 'BX': 1, 'CX': 7,
                 'AY': 8, 'BY': 5, 'CY': 2,
                 'AZ': 3, 'BZ': 9, 'CZ': 6}

with open('input.txt', 'r') as puzzle_input:
    games = puzzle_input.readlines()
    for game in games:
        game = game.replace('\n', '')
        combination = game.replace(' ', '')
        score += alpha_mapping[combination]

print(score)
