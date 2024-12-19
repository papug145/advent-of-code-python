import re
from collections import defaultdict


def print_board(board):
    print('\n'.join(''.join(inner_list) for inner_list in board))
    print()

def solution_2a():
    ans = 0
    lines = open('day_2_p').read().splitlines()
    for id, line in enumerate(lines):
        games = line.strip().split(': ')[1].split('; ')
        for g in games:
            m = defaultdict(int)
            for d in g.split(', '):
                a, b = d.split()
                m[b] = int(a)
            if m['red'] > 12 or m['green'] > 13 or m['blue'] > 14:
                break
        else:
            ans += id+1
    return ans




def solution_2b():
    ans = 0
    lines = open('day_2_p').read().splitlines()
    for id, line in enumerate(lines):
        games = line.strip().split(': ')[1].split('; ')
        m = defaultdict(int)
        for g in games:
            for d in g.split(', '):
                a, b = d.split()
                m[b] = max(int(a), m[b])
        print(m)
        il = 1
        for x in m.values():
            il *= x
        ans += il


    return ans



if __name__ == "__main__":
    print(f'Solution 2a: {solution_2a()}')
    print(f'Solution 2b: {solution_2b()}')
