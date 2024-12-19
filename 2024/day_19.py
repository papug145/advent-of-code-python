import queue
from collections import deque

def solution_19a():
    content = open('day_19_input_1b').read().split('\n\n')
    available = content[0].split(', ')
    desired = content[1].splitlines()
    ans = 0
    cache = {}

    def count(s):
        if s not in cache:
            if len(s) == 0:
                return 1
            else:
                result = 0
                for a in available:
                    if s.startswith(a):
                        result += count(s[len(a):])
                cache[s] = result
        return cache[s]

    for d in desired:
        if count(d) > 0:
            ans += 1
    return ans



def solution_19b():
    content = open('day_19_input_1b').read().split('\n\n')
    available = content[0].split(', ')
    desired = content[1].splitlines()
    ans = 0
    cache = {}

    def count(s):
        if s not in cache:
            if len(s) == 0:
                return 1
            else:
                result = 0
                for a in available:
                    if s.startswith(a):
                        result += count(s[len(a):])
                cache[s] = result
        return cache[s]

    for d in desired:
        ans += count(d)
    return ans

if __name__ == "__main__":
    print(f'Solution 19a: {solution_19a()}')
    print(f'Solution 19b: {solution_19b()}')
