def assembunny(values, instructions):
    i = 0
    while i < len(instructions):
        instr = instructions[i]
        if instr[0] == 'cpy':
            if isinstance(instr[1], int):
                values[instr[2]] = instr[1]
            else:
                values[instr[2]] = values[instr[1]]
            i += 1
        elif instr[0] == 'inc':
            values[instr[1]] += 1
            i += 1
        elif instr[0] == 'dec':
            values[instr[1]] -= 1
            i += 1
        elif instr[0] == 'jnz':
            if (isinstance(instr[1], int) and instr[1] != 0) or (isinstance(instr[1], str) and values[instr[1]] != 0):
                i += instr[2]
            else:
                i += 1
    return values


if __name__ == '__main__':
    with open('day12.txt') as f:
        instructions = f.read().strip().split('\n')
        instructions = [[eval(i) if any(_.isdigit() for _ in i) else i for i in j.split()] for j in instructions]

    values = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    print('Part 1:', assembunny(values, instructions))
    values = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    print('Part 2:', assembunny(values, instructions))