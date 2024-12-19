def solution_4a():
    matrix = []
    with open('day_4_input_1a', 'r') as input_file:
        result_count = 0
        word = ['X', 'M', 'A', 'S']
        for line in input_file:
            row = [c for c in line if c != '\n']
            matrix.append(row)
        directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        nrow = len(matrix)
        ncol = len(matrix[0])
        for i in range(nrow):
            for j in range(ncol):
                for (dx, dy) in directions:
                    n = 0
                    di = i + dx * n
                    dj = j + dy * n
                    while n < 4 and di in range(0, nrow) and dj in range(0, ncol) and matrix[di][dj] == word[n]:
                        n += 1
                        di = i + dx * n
                        dj = j + dy * n
                    if n == 4:
                        result_count += 1
        return result_count


def solution_4b():
    matrix = []
    with open('day_4_input_1a', 'r') as input_file:
        result_count = 0
        for line in input_file:
            row = [c for c in line if c != '\n']
            matrix.append(row)
        nrow = len(matrix)
        ncol = len(matrix[0])
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 'A' and i in range(1, nrow-1) and j in range(1, ncol-1):
                    if {matrix[i - 1][j - 1], matrix[i + 1][j + 1]} == {'M', 'S'} and {matrix[i - 1][j + 1], matrix[i + 1][j - 1]} == {'M', 'S'}:
                        result_count += 1

        return result_count


if __name__ == "__main__":
    print(f'Solution 4a: {solution_4a()}')
    print(f'Solution 4b: {solution_4b()}')
