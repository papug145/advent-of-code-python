from collections import defaultdict


def solution_12a():
    lines = open('day_12_input_1b').read().splitlines()
    board = [list(line.strip()) for line in lines]
    rows = len(board)
    cols = len(board[0])
    fields = {}
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    #  this method is assigning each block with the same letter cluster number fid
    def dfs(x, y, letter, fid):
        if x not in range(rows) or y not in range(cols) or board[x][y] != letter or (x, y) in visited:
            return
        if board[x][y] == letter:
            visited.add((x, y))
            fields[(x, y)] = fid
            for dx, dy in directions:
                dfs(x + dx, y + dy, letter, fid)

    #  here we are iterating over each element in board and assigning cluster number to it
    fid = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                dfs(i, j, board[i][j], fid)
                fid += 1

    #  here we invert cluster so each cluster id is assigned list of nodes that it contains
    fields_by_id = defaultdict(set)
    for (xx, yy), id in fields.items():
        fields_by_id[id].add((xx, yy))

    ans = 0
    for fid, nodes in fields_by_id.items():
        area = len(nodes)
        perimeter = 0
        #  we calculate total perimeter as sum of perimeters for each block
        for x, y in nodes:
            for dx, dy in directions:
                #  if in given direction block has neighbour of different type then it requires +1 perimeter in this direction
                if (x + dx, y + dy) not in nodes:
                    perimeter += 1
        ans += area * perimeter
    return ans


def solution_12b():
    lines = open('day_12_input_1b').read().splitlines()
    board = [list(line.strip()) for line in lines]
    rows = len(board)
    cols = len(board[0])
    fields = {}
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(x, y, letter, fid):
        if x not in range(rows) or y not in range(cols) or board[x][y] != letter or (x, y) in visited:
            return
        if board[x][y] == letter:
            visited.add((x, y))
            fields[(x, y)] = fid
            for dx, dy in directions:
                dfs(x + dx, y + dy, letter, fid)

    fid = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                dfs(i, j, board[i][j], fid)
                fid += 1

    fields_by_id = defaultdict(set)
    for (xx, yy), id in fields.items():
        fields_by_id[id].add((xx, yy))

    ans = 0
    for fid, nodes in fields_by_id.items():
        area = len(nodes)
        perimeter = []
        for x, y in nodes:
            for dx, dy in directions:
                if (x + dx, y + dy) not in nodes:
                    #  here we represent edge as pair of blocks that surround it
                    perimeter.append(((x, y), (x + dx, y + dy)))
        per1 = set(perimeter)
        per2 = set()
        for p1, p2 in per1:
            keep = True
            for dx, dy in [(1, 0), (0, 1)]:  #  checking fence continuation going down and right (not sure why it's not adj4?)
                np1 = (p1[0] + dx, p1[1] + dy)
                np2 = (p2[0] + dx, p2[1] + dy)
                if (np1, np2) in per1:  # if newly created pair is also part of perimeter then we can remove current (p1, p2) because we want only one representant for each edge
                    keep = False
            if keep:
                per2.add((p1, p2))
        ans += area * len(per2)
    return ans


if __name__ == "__main__":
    print(f'Solution 12a: {solution_12a()}')
    print(f'Solution 12b: {solution_12b()}')
