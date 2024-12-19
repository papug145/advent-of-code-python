from collections import defaultdict


def solution_8a():
    board = list(map(list, open('day_8_input_1a').read().splitlines()))
    antennas = defaultdict(list)
    nrows = len(board)
    ncols = len(board[0])
    for i in range(nrows):
        for j in range(ncols):
            if board[i][j] != '.':
                antennas[board[i][j]].append((i, j))
    antynodes = set()
    for node, coordinates in antennas.items():
        print(f'{node}: {coordinates}')
        for i in range(len(coordinates) - 1):
            for j in range(i + 1, len(coordinates)):
                a = coordinates[i]
                b = coordinates[j]
                dx = abs(a[0] - b[0])
                dy = abs(a[1] - b[1])
                ant1 = (a[0] - dx, a[1] - dy if a[1] <= b[1] else a[1] + dy)
                ant2 = (b[0] + dx, b[1] + dy if a[1] <= b[1] else b[1] - dy)
                if ant1[0] in range(nrows) and ant1[1] in range(ncols):
                    antynodes.add(ant1)
                if ant2[0] in range(nrows) and ant2[1] in range(ncols):
                    antynodes.add(ant2)
    return len(antynodes)


def solution_8b():
    board = list(map(list, open('day_8_input_1a').read().splitlines()))
    antennas = defaultdict(list)
    nrows = len(board)
    ncols = len(board[0])

    for i in range(nrows):
        for j in range(ncols):
            if board[i][j] != '.':
                antennas[board[i][j]].append((i, j))

    antynodes = set()
    for node, coordinates in antennas.items():
        print(f'{node}: {coordinates}')
        for i in range(len(coordinates) - 1):
            for j in range(i + 1, len(coordinates)):
                a = coordinates[i]
                b = coordinates[j]
                antynodes.add(a)
                antynodes.add(b)
                dx = abs(a[0] - b[0])
                dy = abs(a[1] - b[1])
                ant1 = (a[0] - dx, a[1] - dy if a[1] <= b[1] else a[1] + dy)
                ant2 = (b[0] + dx, b[1] + dy if a[1] <= b[1] else b[1] - dy)
                while ant1[0] in range(nrows) and ant1[1] in range(ncols):
                    antynodes.add(ant1)
                    ant1 = (ant1[0] - dx, ant1[1] - dy if a[1] <= b[1] else ant1[1] + dy)
                while ant2[0] in range(nrows) and ant2[1] in range(ncols):
                    antynodes.add(ant2)
                    ant2 = (ant2[0] + dx, ant2[1] + dy if a[1] <= b[1] else ant2[1] - dy)
    return len(antynodes)


if __name__ == "__main__":
    print(f'Solution 8a: {solution_8a()}')
    print(f'Solution 8b: {solution_8b()}')
