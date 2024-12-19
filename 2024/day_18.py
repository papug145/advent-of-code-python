import queue
from collections import deque


def print_board(board):
    print('\n'.join(''.join(inner_list) for inner_list in board))
    print()
def solution_18a():
    size = 71
    drop = 1024
    grid = [['.'] * size for _ in range(size)]
    for line in open('day_18_input_1b').read().splitlines()[:drop]:
        x, y = list(map(int, line.split(',')))
        grid[y][x] = '#'

    q = deque()
    q.append((0, 0, 0))
    visited = set()

    while q:
        px, py, dist = q.popleft()
        visited.add((px, py, dist))

        if px == size-1 and py == size-1:
            return dist

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = px + dx, py + dy
            if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and grid[nx][ny] != '#':
                visited.add((nx, ny))
                q.append((nx, ny, dist+1))


def solution_18b():
    size = 71
    grid = [['.'] * size for _ in range(size)]
    for line in open('day_18_input_1b').read().splitlines():
        ans = -1
        x, y = list(map(int, line.split(',')))
        grid[y][x] = '#'

        q = deque()
        q.append((0, 0, 0))
        visited = set()

        while q:
            px, py, dist = q.popleft()
            visited.add((px, py, dist))

            if px == size-1 and py == size-1:
                ans = dist
                break

            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx, ny = px + dx, py + dy
                if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and grid[nx][ny] != '#':
                    visited.add((nx, ny))
                    q.append((nx, ny, dist+1))

        if ans == -1:
            return x, y

if __name__ == "__main__":
    print(f'Solution 18a: {solution_18a()}')
    print(f'Solution 18b: {solution_18b()}')
