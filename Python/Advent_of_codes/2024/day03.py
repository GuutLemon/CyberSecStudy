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
    result = 0
    splitted_inp = []
    do = True
    i = 0
    while i > -1:
        if do:
            found_indx = inp.find("don't()", i)
            do = False
            splitted_inp.append(inp[i:found_indx])
            i = found_indx
        elif not do:
            found_indx = inp.find("do()", i)
            do = True
            i = found_indx
    for s in splitted_inp:
        result += solve_1(s)
    return result


if __name__ == '__main__':
    with open('day03.txt') as f:
        INP = f.read().strip()

    print('Part 1: ', solve_1(INP))
    print('Part 2: ', solve_2(INP))

