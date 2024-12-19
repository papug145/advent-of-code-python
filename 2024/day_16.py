import heapq


def print_board(board):
    print('\n'.join(''.join(inner_list) for inner_list in board))
    print()

def solution_16a():
    board = [list(line) for line in open('day_16_input_1_b').read().splitlines()]
    print_board(board)
    rows = len(board)
    cols = len(board[0])
    start = 0, 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'S':
                start = (i, j)
                break

    visited = set()
    pq = []
    heapq.heappush(pq, (0, start, (0, 1)))
    while pq:
        cost, p, d = heapq.heappop(pq)
        visited.add((p, d))
        if board[p[0]][p[1]] == 'E':
            return cost
        px, py = p
        dx, dy = d
        for new_cost, npx, npy, ndx, ndy in [(cost+1, px+dx, py+dy, dx, dy), (cost+1000, px, py, dy, -dx), (cost+1000, px, py, -dy, dx)]:
            if npx in range(rows) and npy in range(cols) and board[npx][npy] != '#' and ((npx, npy), (ndx, ndy)) not in visited:
                heapq.heappush(pq, (new_cost, (npx, npy), (ndx, ndy)))


def solution_16b():
    board = [list(line) for line in open('day_16_input_1_b').read().splitlines()]
    rows = len(board)
    cols = len(board[0])
    start = 0, 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'S':
                start = (i, j)
                break

    min_costs = {}
    best_paths = []
    pq = []
    heapq.heappush(pq, (0, start, (0, 1), [start]))
    while pq:
        cost, p, d, path = heapq.heappop(pq)

        if board[p[0]][p[1]] == 'E':
            print(f'Solution with cost {cost}')
            print()
            path_board = [[board[i][j] for j in range(cols)] for i in range(rows)]
            for px, py in path:
                path_board[px][py] = '0'
            print_board(path_board)
            if not best_paths or best_paths[0][0] == cost:
                best_paths.append((cost, path))
            elif best_paths[0][0] > cost:
                best_paths = [(cost, path)]
            continue

        if (p, d) in min_costs and min_costs[(p, d)] < cost:
            continue

        min_costs[(p, d)] = cost
        px, py = p
        dx, dy = d
        for new_cost, npx, npy, ndx, ndy in [(cost+1, px+dx, py+dy, dx, dy), (cost+1000, px, py, dy, -dx), (cost+1000, px, py, -dy, dx)]:
            if npx in range(rows) and npy in range(cols) and board[npx][npy] != '#' and new_cost < min_costs.get(((npx, npy), (ndx, ndy)), float("inf")):
                heapq.heappush(pq, (new_cost, (npx, npy), (ndx, ndy), path + [(npx, npy)]))

    best_fields = set(x for _, path in best_paths for x in path)
    return len(best_fields)


if __name__ == "__main__":
    print(f'Solution 16a: {solution_16a()}')
    print(f'Solution 16b: {solution_16b()}')
