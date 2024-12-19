import re

def solution_17a():
    regA, regB, regC, *program = list(map(int, re.findall(r'\d+', open('day_17_input_1b').read())))
    def combo(op):
        if op in [0, 1, 2, 3]:
            return op
        elif op == 4:
            return regA
        elif op == 5:
            return regB
        elif op == 6:
            return regC
        else:
            raise RuntimeError
    i = 0
    output = []
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
        print(opcode, operand)
        if opcode == 0:
            regA = regA // 2**combo(operand)
        elif opcode == 1:
            regB = regB ^ operand
        elif opcode == 2:
            regB = combo(operand) % 8
        elif opcode == 3:
            if regA != 0:
                i = operand
                continue
        elif opcode == 4:
            regB = regB ^ regC
        elif opcode == 5:
            output.append(combo(operand) % 8)
        elif opcode == 6:
            regB = regA // 2 ** combo(operand)
        elif opcode == 7:
            regC = regA // 2**combo(operand)
        i += 2

    return ",".join(str(x) for x in output)


def find(program, ans):
    if not program:
        return ans
    print(program, ans)
    for t in range(8):
        a = (ans << 3) + t
        b = a % 8
        b = b ^ 2
        c = a // 2**b
        b = b ^ 3
        b = b ^ c
        if b % 8 == program[-1]:
            sub = find(program[:-1], a)
            if sub is None: continue
            return sub



def solution_17b():
    _, _, _, *program = list(map(int, re.findall(r'\d+', open('day_17_input_1b').read())))

    return find(program, 0)


if __name__ == "__main__":
    print(f'Solution 17a: {solution_17a()}')
    print(f'Solution 17b: {solution_17b()}')
