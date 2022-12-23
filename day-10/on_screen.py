def print_on_screen(cycle, x):
    if (cycle % 40) - 1 in {x-1, x, x + 1}:
        ans = '#'
    else:
        ans = '.'

    return ans


def main():
    with open('input.txt', 'r') as puzzle_input:
        x = 1
        cycle = 1
        ans = ''

        lines = puzzle_input.readlines()

        for line in lines:
            line = line.replace('\n', '')

            if line == 'noop':
                ans += print_on_screen(cycle, x)
                cycle += 1
            else:
                for i in range(2):
                    ans += print_on_screen(cycle, x)
                    cycle += 1

                value = int(line.split(' ')[-1])
                x += value

        for index in range(0, len(ans), 40):
            print(ans[index: index+41])


if __name__ == '__main__':
    main()
