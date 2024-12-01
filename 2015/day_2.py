import heapq
import math


def solution_2a():
    with open('day_2_input_1a', 'r') as input_file:
        total_area = 0
        for line in input_file:
            l, w, h = map(int, line.split('x'))
            area = 2 * l * w + 2 * w * h + 2 * l * h + math.prod(heapq.nsmallest(2, [l, w, h]))
            total_area += area

        return total_area


def solution_2b():
    with open('day_2_input_1a', 'r') as input_file:
        total_length = 0
        for line in input_file:
            l, w, h = map(int, line.split('x'))
            a, b = heapq.nsmallest(2, [l, w, h])
            length = 2 * a + 2 * b + l * w * h
            total_length += length

        return total_length


if __name__ == "__main__":
    print(f'Solution 2a : {solution_2a()}')
    print(f'Solution 2b : {solution_2b()}')
