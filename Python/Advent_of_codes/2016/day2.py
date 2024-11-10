def find_code(instructions, part):
    directions = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    code = []
    if part == 1:
        keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        current_num = (1, 1)
        for i in instructions:
            for instr in i:
                new_num = tuple(map(sum, zip(current_num, directions[instr])))
                if 0 <= new_num[0] < len(keypad) and 0 <= new_num[1] < len(keypad[0]):
                    current_num = new_num
            code.append(keypad[current_num[0]][current_num[1]])

    elif part == 2:
        keypad = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]
        current_num = (2, 0)
        for i in instructions:
            for instr in i:
                new_num = tuple(map(sum, zip(current_num, directions[instr])))
                if 0 <= new_num[0] < len(keypad) and 0 <= new_num[1] < len(keypad[0]) and keypad[new_num[0]][new_num[1]] != 0:
                    current_num = new_num
            code.append(keypad[current_num[0]][current_num[1]])
    return code


if __name__ == '__main__':
    with open('day2.txt') as f:
        instructions = f.read().strip().split('\n')
    print('Part 1:', find_code(instructions, 1))
    print('Part 2:', find_code(instructions, 2))
