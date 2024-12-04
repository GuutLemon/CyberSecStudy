import re

def mul(x, y):
    return x * y

def solve_1(inp):
    result = 0
    pattern = re.compile(r'mul\(\d+,\d+\)')
    is_valid = pattern.findall(inp)
    for func in is_valid:
        result += eval(func)
    return result

def solve_2(inp):
    valid_seq = ''
    do = True
    i = 0
    while i > -1:
        if do:
            found_indx = inp.find("don't()", i)
            do = False
            valid_seq += inp[i:found_indx]
        else:
            found_indx = inp.find("do()", i)
            do = True
        i = found_indx
    return solve_1(valid_seq)


if __name__ == '__main__':
    with open('day03.txt') as f:
        INP = f.read().strip()

    print('Part 1: ', solve_1(INP))
    print('Part 2: ', solve_2(INP))

