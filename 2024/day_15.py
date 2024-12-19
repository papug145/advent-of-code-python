def print_board(board):
    print('\n'.join(''.join(inner_list) for inner_list in board))
    print()


def solution_15a():
    parts = open('day_15_input_1b').read().split('\n\n')
    board = [list(line) for line in parts[0].splitlines()]
    moves = [m for m in list(parts[1]) if m != '\n']

    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '@':
                rx, ry = i, j

    def move_robot(move):
        nonlocal rx, ry
        instr = {
            '<': (0, -1),
            '^': (-1, 0),
            '>': (0, 1),
            'v': (1, 0)
        }
        mx, my = instr[move]
        cx, cy = rx + mx, ry + my
        to_move = list()
        while board[cx][cy] == 'O':
            to_move.append((cx, cy))
            cx += mx
            cy += my
        if board[cx][cy] != '#':
            board[rx][ry] = '.'
            if to_move:
                board[cx][cy] = 'O'
                nr = to_move[0]
                nrx = nr[0]
                nry = nr[1]
            else:
                nrx, nry = cx, cy
            board[nrx][nry] = '@'
            rx, ry = nrx, nry
        print_board(board)

    for m in moves:
        print(f'After move: {m}')
        move_robot(m)

    ans = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                ans += 100 * i + j
    return ans


def solution_15b():
    parts = open('day_15_input_1b').read().split('\n\n')
    board = [list(line) for line in parts[0].splitlines()]
    moves = [m for m in list(parts[1]) if m != '\n']

    rows = len(board)
    cols = len(board[0])
    newBoard = [[] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '.':
                newBoard[i].append('.')
                newBoard[i].append('.')
            if board[i][j] == '#':
                newBoard[i].append('#')
                newBoard[i].append('#')
            if board[i][j] == 'O':
                newBoard[i].append('[')
                newBoard[i].append(']')
            if board[i][j] == '@':
                newBoard[i].append('@')
                newBoard[i].append('.')

    rows = len(newBoard)
    cols = len(newBoard[0])
    board = newBoard

    print_board(board)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '@':
                rx, ry = i, j

    def move_robot(move):
        nonlocal rx, ry
        nonlocal board
        instr = {
            '<': (0, -1),
            '^': (-1, 0),
            '>': (0, 1),
            'v': (1, 0)
        }
        dx, dy = instr[move]
        to_move = [(rx, ry)]
        i = 0
        impossible = False

        while i < len(to_move):
            nx, ny = to_move[i][0] + dx, to_move[i][1] + dy
            if board[nx][ny] in '[]':
                if (nx, ny) not in to_move:
                    to_move.append((nx, ny))
                if board[nx][ny] == '[':
                    if (nx, ny+1) not in to_move:
                        to_move.append((nx, ny+1))
                if board[nx][ny] == ']':
                    if (nx, ny-1) not in to_move:
                        to_move.append((nx, ny-1))

            elif board[nx][ny] == '#':
                impossible = True
                break
            i += 1

        if impossible:
            print('SHOULD RETURN HERE')
            return
        temp_board = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]
        print(to_move)
        for x,y in to_move:
            temp_board[x][y] = '.'
        for x,y in to_move:
            temp_board[x+dx][y+dy] = board[x][y]

        board = temp_board
        rx, ry = rx+dx, ry+dy
        print_board(board)

    for m in moves:
        print(f'After move: {m}')
        move_robot(m)

    ans = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '[':
                ans += 100 * i + j
    return ans


if __name__ == "__main__":
    #  print(f'Solution 15a: {solution_15a()}')
    print(f'Solution 15b: {solution_15b()}')
