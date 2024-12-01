import hashlib


def solution_4a():
    secret = 'ckczppom'
    result = 1
    while True:
        input_bytes = (secret + str(result)).encode('utf-8')

        if hashlib.md5(input_bytes).hexdigest().startswith('00000'):
            return result
        result += 1


def solution_4b():
    secret = 'ckczppom'
    result = 1
    while True:
        input_bytes = (secret + str(result)).encode('utf-8')

        if hashlib.md5(input_bytes).hexdigest().startswith('000000'):
            return result
        result += 1


if __name__ == "__main__":
    print(f'Solution 4a : {solution_4a()}')
    print(f'Solution 4b : {solution_4b()}')
