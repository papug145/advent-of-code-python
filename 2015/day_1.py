def solution_1a():
    with open('day_1_input_1a', 'r') as input_file:
        data = input_file.read()
        return data.count('(') - data.count(')')


def solution_1b():
    with open('day_1_input_1a', 'r') as input_file:
        data = input_file.read()
        level = 0
        for index, value in enumerate(data):
            if value == '(':
                level += 1
            else:
                level -= 1

            if level < 0:
                return index + 1
    return -1

if __name__ == "__main__":
    print(f'Solution 1a : {solution_1a()}')
    print(f'Solution 1b : {solution_1b()}')
