from functools import cache


def trim_leading_zeros(s):
    trimmed = s.lstrip('0')
    return trimmed if trimmed else '0'


def solution_11a():
    stones = open('day_11_input_1a').read().split()
    print(stones)
    for i in range(25):
        rearranged = []
        for stone in stones:
            if stone == '0':
                rearranged.append('1')
            elif len(stone) % 2 == 0:
                rearranged.append(stone[:int(len(stone) / 2)])
                rearranged.append(trim_leading_zeros(stone[int(len(stone) / 2):]))
            else:
                new_value = str(int(stone) * 2024)
                rearranged.append(new_value)
        stones = rearranged
        print(f'Finished {i}th iteration with {len(stones)} elements')
    return len(stones)


@cache
def count(stone, remained_steps):
    if remained_steps == 0:
        return 1
    if stone == '0':
        return count('1', remained_steps - 1)
    if len(stone) % 2 == 0:
        return count(stone[:len(stone) // 2], remained_steps - 1) + count(trim_leading_zeros(stone[len(stone) // 2:]), remained_steps - 1)
    return count(str(int(stone) * 2024), remained_steps - 1)


def solution_11b():
    stones = open('day_11_input_1b').read().split()
    return sum(count(stone, 75) for stone in stones)


if __name__ == "__main__":
    print(f'Solution 11a: {solution_11a()}')
    print(f'Solution 11b: {solution_11b()}')
