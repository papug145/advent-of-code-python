import re


def solution_5a():
    vowels = 'aeiou'
    forbidden = ['ab', 'cd', 'pq', 'xy']
    result = 0
    with open('day_5_input_1a', 'r') as input_file:
        for line in input_file:
            rule1 = False
            rule2 = False
            rule3 = True
            prev = ''
            vowel_count = 0
            for char in line:
                if not rule1 and char in vowels:
                    vowel_count += 1
                    if vowel_count >= 3:
                        rule1 = True
                if not rule2 and char == prev:
                    rule2 = True
                if prev + char in forbidden:
                    rule3 = False
                    break
                prev = char
            if rule1 and rule2 and rule3:
                result += 1
    return result


def solution_5b():
    pattern1 = r'([a-zA-Z]{2}).*?\1'
    pattern2 = r'([a-zA-Z]).\1'
    result = 0
    with open('day_5_input_1a', 'r') as input_file:
        for line in input_file:
            if bool(re.search(pattern1, line)) and bool(re.search(pattern2, line)):
                result += 1
    return result


if __name__ == "__main__":
    print(f'Solution 5a : {solution_5a()}')
    print(f'Solution 5b : {solution_5b()}')
