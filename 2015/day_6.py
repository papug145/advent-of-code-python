import re


def solution_6a():
    pattern = r'(\d+),(\d+) through (\d+),(\d+)'

    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    with open('day_6_input_1a', 'r') as input_file:
        for line in input_file:
            match = re.search(pattern, line)
            x0, y0 = int(match.group(1)), int(match.group(2))
            x1, y1 = int(match.group(3)), int(match.group(4))

            if line.startswith('turn on'):
                for i in range(x0, x1 + 1):
                    for j in range(y0, y1 + 1):
                        grid[i][j] = 1
            if line.startswith('turn off'):
                for i in range(x0, x1 + 1):
                    for j in range(y0, y1 + 1):
                        grid[i][j] = 0
            if line.startswith('toggle'):
                for i in range(x0, x1 + 1):
                    for j in range(y0, y1 + 1):
                        grid[i][j] = 1 - grid[i][j]

    return sum(sum(row) for row in grid)


def solution_6b():
    pattern = r'(\d+),(\d+) through (\d+),(\d+)'

    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    with open('day_6_input_1a', 'r') as input_file:
        for line in input_file:
            match = re.search(pattern, line)
            x0, y0 = int(match.group(1)), int(match.group(2))
            x1, y1 = int(match.group(3)), int(match.group(4))

            if line.startswith('turn on'):
                for i in range(x0, x1 + 1):
                    for j in range(y0, y1 + 1):
                        grid[i][j] += 1
            if line.startswith('turn off'):
                for i in range(x0, x1 + 1):
                    for j in range(y0, y1 + 1):
                        grid[i][j] = max(0, grid[i][j]-1)
            if line.startswith('toggle'):
                for i in range(x0, x1 + 1):
                    for j in range(y0, y1 + 1):
                        grid[i][j] += 2

    return sum(sum(row) for row in grid)


if __name__ == "__main__":
    print(f'Solution 6a : {solution_6a()}')
    print(f'Solution 6b : {solution_6b()}')
