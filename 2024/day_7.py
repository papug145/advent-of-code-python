from itertools import chain, combinations
def solution_7a():
    result = 0
    with open('day_7_input_1a', 'r') as input:
        for line in input:
            test_value = int(line.split(':')[0].strip())
            numbers = list(map(int, line.split(':')[1].split()))
            subsets = generate_subsets_from_range(len(numbers))
            for subset in subsets:
                local_result = numbers[0]
                for i in range(1, len(numbers)):
                    if i in subset:
                        local_result *= numbers[i]
                    else:
                        local_result += numbers[i]
                if local_result == test_value:
                    result += test_value
                    break
    return result

def solution_7b():
    result = 0
    with open('day_7_input_1a', 'r') as input:
        for line in input:
            test_value = int(line.split(':')[0].strip())
            numbers = list(map(int, line.split(':')[1].split()))
            subsets = generate_divisions_into_three_subsets(list(range(len(numbers))))
            for subset in subsets:
                local_result = numbers[0]
                for i in range(1, len(numbers)):
                    if i in subset[0]:
                        local_result *= numbers[i]
                    elif i in subset[1]:
                        local_result += numbers[i]
                    else:
                        local_result = int(str(local_result) + str(numbers[i]))
                if local_result == test_value:
                    result += test_value
                    break
    return result


def generate_divisions_into_three_subsets(numbers):
    divisions = []
    n = len(numbers)
    numbers = list(numbers)

    # Iterate over all possible ways to partition into 3 subsets
    for size1 in range(n + 1):
        for subset1 in combinations(numbers, size1):
            remaining = set(numbers) - set(subset1)
            for size2 in range(len(remaining) + 1):
                for subset2 in combinations(remaining, size2):
                    subset3 = remaining - set(subset2)
                    divisions.append((list(subset1), list(subset2), list(subset3)))

    return divisions


def generate_subsets_from_range(end):
    # Create a range of numbers
    num_range = range(end)
    # Generate all subsets
    subsets = chain.from_iterable(combinations(num_range, r) for r in range(len(num_range) + 1))
    return list(subsets)


if __name__ == "__main__":
    print(f'Solution 7a: {solution_7a()}')
    print(f'Solution 7b: {solution_7b()}')
