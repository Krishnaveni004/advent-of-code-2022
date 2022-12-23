with open('input.txt', 'r') as puzzle_input:
    x = 1
    cycle = 0
    ans = 0

    required = set(range(20, 221, 40))
    array = []
    lines = puzzle_input.readlines()

    for line in lines:
        line = line.replace('\n', '')
        if line == 'noop':
            array.append(x)
        else:
            value = int(line.split(' ')[-1])
            array.extend([x, x])  # first cycle, second cycle

            x += value
            cycle += 1

            if cycle in required:
                ans += cycle * array[cycle-1]

        cycle += 1

        if cycle in required:
            ans += cycle * array[cycle-1]

    print(ans)
