import re


def solution_3a():
    with open('day_3_input_1a', 'r') as input_file:
        result = 0
        content = input_file.read()
        for match in re.findall(r'mul\((\d+),(\d+)\)', content):
            result += int(match[0]) * int(match[1])
        return result


def solution_3b():
    with open('day_3_input_1a', 'r') as input_file:
        result = 0
        content = input_file.read()
        end_index = len(content)
        start = 0
        while start != -1:
            end = content.find("don't()", start)
            print(f"don't() found on {end}")
            if end == -1:
                end = end_index
            for match in re.findall(r'mul\((\d+),(\d+)\)', content[start:end]):
                result += int(match[0]) * int(match[1])
            start = content.find("do()", end+len("don't()"))
            print(f"do() found at {start}")
    return result


if __name__ == "__main__":
    print(f'Solution 3a: {solution_3a()}')
    print(f'Solution 3b: {solution_3b()}')