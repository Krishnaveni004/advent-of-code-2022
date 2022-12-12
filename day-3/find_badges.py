from itertools import islice

from rucksack_reorg import calculate_priority

score = 0

with open('input.txt', 'r') as puzzle_input:
    next_group = list(islice(puzzle_input, 3))
    while next_group:
        bag1, bag2, bag3 = map(lambda x: x.replace('\n', ''), next_group)
        badge = set(bag1).intersection(set(bag2).intersection(set(bag3)))

        score += calculate_priority(badge.pop())
        next_group = list(islice(puzzle_input, 3))

print(score)
