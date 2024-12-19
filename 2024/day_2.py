#  REVIEWED

def solution_2a():
    with open('day_2_input_1a', 'r') as input_file:
        result = 0
        for line in input_file:
            levels = list(map(int, line.split()))
            if are_valid(levels):
                result += 1
    return result


def are_valid(levels):
    steps = [a[0] - a[1] for a in zip(levels[:-1], levels[1:])]
    return all(1 <= step <= 3 for step in steps) or all(-1 >= step >= -3 for step in steps)


def solution_2b():
    with open('day_2_input_1a', 'r') as input_file:
        result = 0
        for line in input_file:
            levels = list(map(int, line.split()))
            #  HyperNeutrino shorter syntax
            #  if any(are_valid(levels[:i] + levels[i+1:]) for i in range(len(levels))):
            #    result += 1
            if are_valid(levels):
                print(f"Original levels tested positive: {levels}")
                result += 1
            else:
                print(f"Original levels tested negative: {levels}")
                for i in range(len(levels)):
                    modified = levels[:i] + levels[i + 1:]
                    print(f"Checking modified levels: {modified}")
                    if are_valid(modified):
                        print("TESTED POSITIVE after modification")
                        result += 1
                        break
    return result


if __name__ == "__main__":
    print(f'Solution 2a: {solution_2a()}')
    print(f'Solution 2b: {solution_2b()}')