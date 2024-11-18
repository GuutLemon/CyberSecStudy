def count_steps(lst, part):
    i = 0
    steps = 0
    while True:
        try:
            jump_value = lst[i]
        except IndexError:
            return steps
        if part == 2 and jump_value >= 3:
            lst[i] -= 1
        else:
            lst[i] += 1
        i += jump_value
        steps += 1


if __name__ == '__main__':
    with open('day05.txt') as f:
        instructions = f.read().strip().split('\n')
        instructions = [eval(i) for i in instructions]

    print('Part 1: ', count_steps(instructions.copy(), 1))
    print('Part 2: ', count_steps(instructions.copy(), 2))