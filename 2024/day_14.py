import re
from collections import defaultdict


def solution_14a():
    width = 101
    height = 103
    q1 = q2 = q3 = q4 = 0
    lines = open('day_14_input_1b').read().splitlines()
    for line in lines:
        spos = re.search(r'p=(\d+),(\d+)', line)
        px, py = int(spos[1]), int(spos[2])
        vel = re.search(r'v=(-?\d+),(-?\d+)', line)
        vx, vy = int(vel[1]), int(vel[2])
        print(px, py, vx, vy)
        for _ in range(100):
            px = (px + vx) % width
            py = (py + vy) % height
            print(px, py)
        if px in range(width // 2) and py in range(height // 2):
            q1 += 1
        if px in range(width // 2+1, width) and py in range(height // 2):
            q2 += 1
        if px in range(width // 2) and py in range(height // 2 + 1, height):
            q3 += 1
        if px in range(width // 2+1, width) and py in range(height // 2 + 1, height):
            q4 += 1

    return q1*q2*q3*q4



def solution_14b():
    pass



if __name__ == "__main__":
    print(f'Solution 14a: {solution_14a()}')
    print(f'Solution 14b: {solution_14b()}')
