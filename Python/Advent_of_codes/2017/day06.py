def debugging(inp):
    steps = 0
    redistributed = inp.copy()
    states = []
    while states.count(redistributed) == 1 or steps == 0:
        max_value = max(redistributed)
        max_indx = redistributed.index(max_value)
        redistributed[max_indx] = 0
        for i in range(max_value):
            next_indx = (max_indx + 1 + i) % len(redistributed)
            redistributed[next_indx] += 1
        states.append(redistributed.copy())
        steps += 1
    loop_len = len(states) - 1 - states.index(redistributed)
    return steps, loop_len


if __name__ == '__main__':
    BLOCKS = '2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14'
    BLOCKS = [int(_) for _ in BLOCKS.split()]

    print('Part 1: ', debugging(BLOCKS)[0])
    print('Part 2: ', debugging(BLOCKS)[1])

