import re
from collections import defaultdict


def solution_5a():
    results = []
    pattern = re.compile(r'(\d+)\|(\d+)')
    banned = defaultdict(list)
    with open('day_5_input_1a', 'r') as rules:
        for rule in rules:
            match = re.match(pattern, rule)
            x, y = int(match.group(1)), int(match.group(2))
            banned[y].append(x)
    with open('day_5_input_1b', 'r') as updates:
        for update in updates:
            order = list(map(int, update.split(',')))
            local_banned = []
            failed = False
            for number in order:
                if number in local_banned:
                    failed = True
                    break
                else:
                    local_banned.extend(banned[number])
            if not failed:
                results.append(order[int(len(order) / 2)])
    return sum(results)


def solution_5b():
    failed_results = []
    pattern = re.compile(r'(\d+)\|(\d+)')
    banned = defaultdict(list)
    with open('day_5_input_1a', 'r') as rules:
        for rule in rules:
            match = re.match(pattern, rule)
            x, y = int(match.group(1)), int(match.group(2))
            banned[y].append(x)
    with open('day_5_input_1b', 'r') as updates:
        for update in updates:
            order = list(map(int, update.split(',')))
            local_banned = []
            failed = False
            for number in order:
                if number in local_banned:
                    failed = True
                    break
                else:
                    local_banned.extend(banned[number])
            if failed:
                failed_results.append(order)
        for failed in failed_results:
            print(f'Failed before processing: {failed}')
            for i in range(len(failed)):
                for j in range(i + 1, len(failed)):
                    if failed[j] in banned[failed[i]]:
                        temp = failed[j]
                        failed[j] = failed[i]
                        failed[i] = temp
            print(f'Failed after processing: {failed}')

        return sum([f[int(len(f) / 2)] for f in failed_results])


if __name__ == "__main__":
    print(f'Solution 5a: {solution_5a()}')
    print(f'Solution 5b: {solution_5b()}')
