import re
from collections import defaultdict


def print_board(board):
    print('\n'.join(''.join(inner_list) for inner_list in board))
    print()

def solution_1a():
    ans = 0
    lines = open('day_1_p').read().splitlines()
    for line in lines:
        digits = re.findall(r'\d', line)
        print(digits)
        ans += int(digits[0]) * 10 + int(digits[-1])
    return ans




def solution_1b():
    ans = 0
    n = 'one two three four five six seven eight nine'.split()

    def convert(a):
        if a in n:
            return str(n.index(a) + 1)
        else:
            return a


    pattern = '(?=(' + '|'.join(n) + '|\\d))'
    lines = open('day_1_p').read().splitlines()
    for line in lines:
        found = re.findall(pattern, line)
        print(found)
        ans += int(convert(found[0]) + convert(found[-1]))
    return ans



if __name__ == "__main__":
    print(f'Solution 1a: {solution_1a()}')
    print(f'Solution 1b: {solution_1b()}')
