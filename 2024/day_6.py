
def solution_6a():
    board = [list(line.strip()) for line in open('day_6_input_1a').read().splitlines()]
    nrows = len(board)
    ncols = len(board[0])
    visited = set()
    for i in range(nrows):
        for j in range(ncols):
            if board[i][j] == '^':
                break
        else:  # only executed if there was no break
            continue
        break

    dr = -1
    dc = 0

    while True:
        visited.add((i, j))
        if not (i + dr in range(nrows) and j + dc in range(ncols)):
            break
        if board[i + dr][j + dc] == '#':
            dr, dc = dc, -dr
        else:
            i += dr
            j += dc
    return len(visited)




def solution_6b():
    board = [list(line.strip()) for line in open('day_6_input_1b').read().splitlines()]
    nrows = len(board)
    ncols = len(board[0])
    visited = set()
    for i in range(nrows):
        for j in range(ncols):
            if board[i][j] == '^':
                break
        else:  # only executed if there was no break
            continue
        break

    def has_loops(r, c, dr, dc):
        visited = set()
        while True:
            if (r, c, dr, dc) in visited:
                return True
            visited.add((r, c, dr, dc))
            if not (r + dr in range(nrows) and c + dc in range(ncols)):
                break
            if board[r + dr][c + dc] == '#':
                dr, dc = dc, -dr
            else:
                r += dr
                c += dc
        return False

    result = 0
    for k in range(nrows):
        for l in range(ncols):
            if board[k][l] == '.':
                board[k][l] = '#'
                if has_loops(i, j, -1, 0):
                    result += 1
                board[k][l] = '.'
    return result


if __name__ == "__main__":
    print(f'Solution 6a: {solution_6a()}')
    print(f'Solution 6b: {solution_6b()}')
