def solution_9a():
    disk = list(open('day_9_input_1b').read())
    fid = 0
    representation = []
    for (i, elem) in enumerate(disk):
        value = int(elem)
        if i % 2 == 0:
            representation += [fid] * value
            fid += 1
        else:
            representation += [-1] * value
    blanks = [i for i, x in enumerate(representation) if x == -1]
    print(blanks)
    for i in blanks:
        while representation[-1] == -1:
            representation.pop()
        if len(representation) <= i:
            break
        representation[i] = representation.pop()
    return sum(i * x for i, x in enumerate(representation))


def solution_9b():
    input = list(open('day_9_input_1b').read())
    print(input)
    files = {}
    blanks = []
    fid = 0
    pos = 0
    for i, elem in enumerate(input):
        value = int(elem)
        if i % 2 == 0:
            files[fid] = (pos, value)
            fid += 1
        else:
            if value != 0:
                blanks.append((pos, value))
        pos += value
    print(f'Files before: {files}')
    print(f'Blanks before: {blanks}')

    fid -= 1
    while fid >= 0:
        file_start, file_size = files.get(fid)
        for i, (blank_start, blank_size) in enumerate(blanks):
            if blank_start >= file_start:
                blanks = blanks[:i]
                break
            if file_size == blank_size:
                files[fid] = (blank_start, file_size)
                blanks.pop(i)
                break
            if file_size < blank_size:
                files[fid] = (blank_start, file_size)
                blanks[i] = (blank_start + file_size, blank_size - file_size)
                break
        fid -= 1
    print(f'Files after: {files}')
    print(f'Blanks after: {blanks}')
    result = 0
    for fid, (start, size) in files.items():
        for i in range(start, start + size):
            result += fid * i
    return result


if __name__ == "__main__":
    print(f'Solution 9a: {solution_9a()}')
    # print(f'Solution 9b: {solution_9b()}')
