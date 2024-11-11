import re
from collections import defaultdict

def register(instructions):
    bots = defaultdict(list)
    outputs = defaultdict(int)
    for instr in instructions:
        if not isinstance(instr, list):
            instr = instr.split()
            value = int(instr[1])
            if not bots[instr[2]]:
                bots[instr[2]] = [[], set()]
            bots[instr[2]][0].append(value)
            bots[instr[2]][1].add(value)
        else:
            for i in instr:
                if 'output' in i:
                    outputs[i[6:]] = 0
                elif not bots[i]:
                    bots[i] = [[], set()]
    return bots, outputs

def sort_chips(bots, outputs, instr):
    if isinstance(instr, list):
        chips = sorted(bots[instr[0]][0])
        if len(chips) == 2:
            for i in range(2):
                if 'output' in instr[i+1]:
                    output_num = instr[i+1]
                    outputs[output_num[6:]] = chips[i]
                else:
                    bots[instr[i+1]][0].append(chips[i])
                    bots[instr[i+1]][1].add(chips[i])
            bots[instr[0]][0] = []
    return bots, outputs


if __name__ == '__main__':
    with open('day10.txt') as f:
        instructions = f.read().strip()
        instructions = re.sub(r'gives low to |and high to |goes to |bot ', '', instructions)
        instructions = re.sub(r'output ', 'output', instructions)
        instructions = instructions.split('\n')
        instructions = [_.split() if not _.startswith('value') else _ for _ in instructions]

    reg = register(instructions)
    bots = reg[0]
    outputs = reg[1]

    while not all(i != 0 for i in outputs.values()):
        for instr in instructions:
            bots, outputs = sort_chips(bots, outputs, instr)
    for b in bots:
        if bots[b][1] == {61, 17}:
            print('Part 1:', b)

    value = outputs['0'] * outputs['1'] * outputs['2']
    print('Part 2:', value)