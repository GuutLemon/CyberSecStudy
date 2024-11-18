from collections import defaultdict


def execute_instr(lst):
    reg = defaultdict(int)
    record_value = 0
    for instr in lst:
        register = instr[0]
        if instr[1] == 'inc':
            value = int(instr[2])
        else:
            value = -int(instr[2])
        cond = ' '.join(instr[3:])
        if eval(cond):
            reg[register] += value
        current_max_value = max(reg.values())
        record_value = max(current_max_value, record_value)
    return current_max_value, record_value


if __name__ == '__main__':
    with open('day08.txt') as f:
        instructions = f.read().strip().replace('if ', '').split('\n')
        instructions = [_.split() for _ in instructions]
        instructions = [[f'reg["{j[i]}"]' if i == 3 else j[i] for i in range(len(j))] for j in instructions]

    solve = execute_instr(instructions)
    print('Part 1: ', solve[0])
    print('Part 2: ', solve[1])
