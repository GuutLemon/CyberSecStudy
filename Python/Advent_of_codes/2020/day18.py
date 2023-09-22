import re

with open('day18.txt') as f:
    read_data = f.read().strip().split('\n')


def eval_part1(l):
    # Turn line into something like (((1 + 2) * 3) + 4) then eval
    open_count = len(range(2, len(l) - 2, 2))
    l[0] = '(' * open_count + l[0]
    for i in range(2, len(l) - 2, 2):
        l[i] = l[i] + ')'
    # print(l)
    return eval(''.join(l))


def eval_part2(l):
    l = ''.join(l)
    l = '(' + l.replace('*', ')*(') + ')'
    return eval(l)


def eval_line(l):
    if len(l.split()) == 3:
        return eval(l)
    # Get everything in most outer ()
    # This is the hard part
    pattern = r'\((?:[^()]*|\(*[^()]*\))*\)'
    in_parentheses = re.findall(pattern, l)
    # Eval stuffs in most outer (), remove ()
    in_parentheses = [eval_line(_[1:-1]) for _ in in_parentheses]
    # Turn line in something like '1 * in + in + 4' then match 'in' with their recursive eval results
    in_parentheses_pos = []
    if in_parentheses:
        l = re.sub(pattern, 'in', l)
        l = l.split()
        # print(l, in_parentheses)
        for i in range(len(l)):
            if l[i] == 'in':
                in_parentheses_pos.append(i)
        for i in range(len(in_parentheses)):
            l[in_parentheses_pos[i]] = str(in_parentheses[i])
        return eval_part2(l)
    else:
        l = l.split()
        return eval_part2(l)


result = 0
for l in read_data:
    result += eval_line(l)
print(result)