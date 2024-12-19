import re
from collections import defaultdict


def solution_13a():
    content = open('day_13_input_1b').read()
    buttonA = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
    buttonB = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
    prize = re.compile(r'Prize: X=(\d+), Y=(\d+)')

    matchA = re.findall(buttonA, content)
    matchB = re.findall(buttonB, content)
    matchPrize = re.findall(prize, content)

    ans = 0
    for i in range(len(matchA)):
        ax, ay = int(matchA[i][0]), int(matchA[i][1])
        bx, by = int(matchB[i][0]), int(matchB[i][1])
        px, py = int(matchPrize[i][0]), int(matchPrize[i][1])
        print(ax, ay, bx, by, px, py)

        nb = 100
        while nb >= 0:
            xrem = px - bx * nb
            yrem = py - by * nb
            print(xrem, yrem)

            if xrem % ax == 0 and yrem % ay == 0 and xrem // ax == yrem // ay:
                ans += nb + 3 * (xrem // ax)
                break
            nb -= 1

    return ans






def solution_13b():
    modificator = 10_000_000_000_000
    content = open('day_13_input_1b').read()
    buttonA = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
    buttonB = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
    prize = re.compile(r'Prize: X=(\d+), Y=(\d+)')

    matchA = re.findall(buttonA, content)
    matchB = re.findall(buttonB, content)
    matchPrize = re.findall(prize, content)

    ans = 0
    for i in range(len(matchA)):
        ax, ay = int(matchA[i][0]), int(matchA[i][1])
        bx, by = int(matchB[i][0]), int(matchB[i][1])
        px, py = modificator + int(matchPrize[i][0]), modificator + int(matchPrize[i][1])

        na = (by*px - bx*py) / (by*ax - bx*ay)
        nb = (px - ax*na) / bx

        if na == int(na) and nb == int(nb):
            ans += nb + 3 * na

        print(na, nb)

    return ans



if __name__ == "__main__":
    #  print(f'Solution 13a: {solution_13a()}')
    print(f'Solution 13b: {solution_13b()}')
