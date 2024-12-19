from collections import defaultdict


def solution_10a():
    lines = list(map(list, open('day_10_input_1b').read().splitlines()))
    matrix = [[int(x) for x in row] for row in lines]

    rows = len(matrix)
    cols = len(matrix[0])
    result = 0
    visited_from = defaultdict(set)
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def traverse(r, c, level):
        nonlocal result
        nonlocal visited_from
        nonlocal i, j
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if nr in range(rows) and nc in range(cols) and matrix[nr][nc] == level + 1:
                print(f'Looking at position ({nr, nc}) with value {matrix[nr][nc]} at searched level {level + 1}')
                if level + 1 == 9 and (nr, nc) not in visited_from[(i, j)]:
                    result += 1
                    visited_from[(i, j)].add((nr, nc))
                    print(f'Increasing result to {result}')
                else:
                    traverse(nr, nc, level + 1)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                before = result
                traverse(i, j, 0)
                print(f'For {i}, {j} trailhead score is {result - before}')

    return result


def solution_10b():
    lines = list(map(list, open('day_10_input_1b').read().splitlines()))
    matrix = [[int(x) for x in row] for row in lines]

    rows = len(matrix)
    cols = len(matrix[0])
    result = 0
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def traverse(r, c, level):
        nonlocal result
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if nr in range(rows) and nc in range(cols) and matrix[nr][nc] == level + 1:
                print(f'Looking at position ({nr, nc}) with value {matrix[nr][nc]} at searched level {level + 1}')
                if level + 1 == 9:
                    result += 1
                    print(f'Increasing result to {result}')
                else:
                    traverse(nr, nc, level + 1)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                before = result
                traverse(i, j, 0)
                print(f'For {i}, {j} trailhead score is {result - before}')

    return result


if __name__ == "__main__":
    print(f'Solution 10a: {solution_10a()}')
    print(f'Solution 10b: {solution_10b()}')
