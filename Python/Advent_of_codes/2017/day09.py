def scoring(inp):
    score = 0
    depth = 0
    garbage = False
    ignore = False
    garbage_content = 0
    for c in inp:
        if not garbage and c == '<':
            garbage = True
        elif garbage:
            if ignore:
                ignore = False
                continue
            if c == '!':
                ignore = True
            elif c == '>':
                garbage = False
            else:
                garbage_content += 1

        elif not garbage:
            if c == '{':
                depth += 1
            elif c == '}' and depth > 0:
                score += depth
                depth -= 1
    return score, garbage_content


if __name__ == '__main__':
    with open('day09.txt') as f:
        INP = f.read().strip()

    print('Part 1: ', scoring(INP)[0])
    print('Part 2: ', scoring(INP)[1])