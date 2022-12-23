def main():
    with open('input.txt', 'r') as puzzle_input:
        readable = puzzle_input.readlines()

        grid = []
        for line in readable:
            line = line.replace('\n', '')
            grid.append(list(map(int, list(line))))

        m, n = len(grid), len(grid[0])
        visibility_matrix = [[[0, 0, 0, 0] for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(1, n):
                for k in range(j-1, -1, -1):
                    if grid[i][k] >= grid[i][j]:
                        visibility_matrix[i][j][0] += 1
                        break
                    visibility_matrix[i][j][0] += 1

                for k in range(j+1, n):
                    if grid[i][k] >= grid[i][j]:
                        visibility_matrix[i][j][1] += 1
                        break
                    visibility_matrix[i][j][1] += 1

        for j in range(n):
            for i in range(1, m):
                for k in range(i-1, -1, -1):
                    if grid[k][j] >= grid[i][j]:
                        visibility_matrix[i][j][2] += 1
                        break
                    visibility_matrix[i][j][2] += 1

                for k in range(i+1, m):
                    if grid[k][j] >= grid[i][j]:
                        visibility_matrix[i][j][3] += 1
                        break
                    visibility_matrix[i][j][3] += 1

        max_value = 0
        for i in range(m):
            for j in range(n):
                value = visibility_matrix[i][j][0] * visibility_matrix[i][j][1] * visibility_matrix[i][j][2] * visibility_matrix[i][j][3]
                max_value = max(max_value, value)

            print(visibility_matrix[i])
        print(max_value)


if __name__ == '__main__':
    main()
