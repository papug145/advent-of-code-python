import heapq


def solution_1a():
    with open('day_1_input_1a', 'r') as input_file:
        left = []
        right = []
        for line in input_file:
            ids = list(map(int, line.split()))
            heapq.heappush(left, ids[0])
            heapq.heappush(right, ids[1])
    return sum([abs(heapq.heappop(left) - heapq.heappop(right)) for _ in range(len(left))])


def solution_1b():
    with open('day_1_input_1a', 'r') as input_file:
        left = list()
        right = dict()
        for line in input_file:
            ids = list(map(int, line.split()))
            left.append(ids[0])
            right[ids[1]] = right.get(ids[1], 0) + 1
        result = 0
        for id in left:
            result += right.get(id, 0) * id
    return result


if __name__ == "__main__":
    print(f'Solution 1a: {solution_1a()}')
    print(f'Solution 1b: {solution_1b()}')
