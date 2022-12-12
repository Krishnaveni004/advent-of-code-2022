count = 0

with open('input.txt', 'r') as puzzle_input:
    sections = puzzle_input.readlines()
    for section in sections:
        assgn1, assgn2 = section.split(',')
        start1, end1 = map(int, assgn1.split('-'))
        start2, end2 = map(int, assgn2.split('-'))

        if max(start1, start2) <= min(end1, end2):
            count += 1

print(count)
