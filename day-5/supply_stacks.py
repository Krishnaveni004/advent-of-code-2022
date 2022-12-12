from collections import defaultdict,  deque

with open('input.txt', 'r') as puzzle_input:
    supply_stacks = defaultdict(deque)
    readable = puzzle_input.readlines()

    for line in readable:
        if '[' in line:
            for index, value in enumerate(range(1, len(line), 4)):
                if line[value] != ' ':
                    supply_stacks[index+1].appendleft(line[value])

        elif line.startswith(' 1') or line == '\n':
            continue

        else:
            # move 2 from 4 to 6
            count, directions = line.split('from')
            count = int(count.split('move')[1].strip())

            _from, to = map(int, directions.split('to'))

            for index in range(count):
                supply_stacks[to].append(supply_stacks[_from].pop())

    result = ''
    for key in sorted(supply_stacks):
        result += supply_stacks[key][-1]

    print(result)
