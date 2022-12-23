from common import generate_visibility_matrix


class FontColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_visible(grid, arr, i, j, m, n):
    visibility = False

    if i in [0, m - 1] or j in [0, n - 1]:
        visibility = True
    else:
        for k in range(4):
            if grid[i][j] > arr[i][j][k]:
                visibility = True

    return visibility


def main():
    grid, visibility_matrix, m, n = generate_visibility_matrix()

    visible = 0
    colors = {True: FontColor.OKGREEN + FontColor.BOLD, False: FontColor.FAIL}
    for i in range(m):
        for j in range(n):
            visibility = is_visible(grid, visibility_matrix, i, j, m, n)
            color = colors[visibility]
            visible += visibility
            print(f'{color}{visibility_matrix[i][j]}{FontColor.ENDC}', end=', ')
        print('')

    print(visible)


if __name__ == '__main__':
    main()
