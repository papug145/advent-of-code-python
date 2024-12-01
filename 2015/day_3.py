def solution_3a():
    with open('day_3_input_1a', 'r') as input_file:
        pos = (0, 0)
        visited = set()
        visited.add(pos)
        for direction in input_file.read():
            if direction == '^':
                pos = (pos[0], pos[1] + 1)
            elif direction == '>':
                pos = (pos[0] + 1, pos[1])
            elif direction == 'v':
                pos = (pos[0], pos[1] - 1)
            elif direction == '<':
                pos = (pos[0] - 1, pos[1])

            visited.add(pos)
        return len(visited)


def solution_3b():
    with open('day_3_input_1a', 'r') as input_file:
        santa_pos = (0, 0)
        robo_santa_pos = (0, 0)
        visited = set()
        visited.add((0, 0))
        for index, direction in enumerate(input_file.read()):
            if direction == '^':
                if index % 2 == 0:
                    santa_pos = (santa_pos[0], santa_pos[1] + 1)
                else:
                    robo_santa_pos = (robo_santa_pos[0], robo_santa_pos[1] + 1)
            elif direction == '>':
                if index % 2 == 0:
                    santa_pos = (santa_pos[0] + 1, santa_pos[1])
                else:
                    robo_santa_pos = (robo_santa_pos[0] + 1, robo_santa_pos[1])
            elif direction == 'v':
                if index % 2 == 0:
                    santa_pos = (santa_pos[0], santa_pos[1] - 1)
                else:
                    robo_santa_pos = (robo_santa_pos[0], robo_santa_pos[1] - 1)
            elif direction == '<':
                if index % 2 == 0:
                    santa_pos = (santa_pos[0] - 1, santa_pos[1])
                else:
                    robo_santa_pos = (robo_santa_pos[0] - 1, robo_santa_pos[1])

            visited.add(santa_pos)
            visited.add(robo_santa_pos)
        return len(visited)


if __name__ == "__main__":
    print(f'Solution 3a : {solution_3a()}')
    print(f'Solution 3b : {solution_3b()}')
