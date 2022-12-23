def generate_visibility_matrix():
    with open('input.txt', 'r') as puzzle_input:
        readable = puzzle_input.readlines()

        grid = []
        for line in readable:
            line = line.replace('\n', '')
            grid.append(list(map(int, list(line))))

        m, n = len(grid), len(grid[0])
        visibility_matrix = [[[0, 0, 0, 0] for i in range(n)] for j in range(m)]

        # Left Max
        for i in range(m):
            for j in range(1, n):
                if j == 1:
                    visibility_matrix[i][j][0] = grid[i][j - 1]
                else:
                    visibility_matrix[i][j][0] = max(visibility_matrix[i][j - 1][0], grid[i][j - 1])

        # Right Max
        for i in range(m - 1, -1, -1):
            for j in range(n - 2, -1, -1):
                if j == n - 2:
                    visibility_matrix[i][j][1] = grid[i][j+1]
                else:
                    visibility_matrix[i][j][1] = max(visibility_matrix[i][j + 1][1], grid[i][j + 1])

        # Top Max
        for j in range(n):
            for i in range(1, m):
                if i == 1:
                    visibility_matrix[i][j][2] = grid[i - 1][j]
                else:
                    visibility_matrix[i][j][2] = max(visibility_matrix[i - 1][j][2], grid[i - 1][j])

        # Bottom Max
        for j in range(n - 1, -1, -1):
            for i in range(m - 2, -1, -1):
                if i == m - 2:
                    visibility_matrix[i][j][3] = grid[i + 1][j]
                else:
                    visibility_matrix[i][j][3] = max(visibility_matrix[i + 1][j][3], grid[i + 1][j])

    return grid, visibility_matrix, m, n
