with open('day2.txt') as f:
    read_data = f.read().strip()
    processed_data = eval('['+read_data+']')

# Part 1
inp = processed_data[::]
inp[1] = 12
inp[2] = 2
def find_first_num(inp):
    for i in range(0, len(inp), 4):
        if inp[i] == 1:
            inp[inp[i + 3]] = inp[inp[i + 1]] + inp[inp[i + 2]]
        elif inp[i] == 2:
            inp[inp[i + 3]] = inp[inp[i + 1]] * inp[inp[i + 2]]
        elif inp[i] == 99:
            break
    return inp[0]
print(find_first_num(inp))

# Part 2
def part2(inp):
    for i in range(100):
        for j in range(100):
            inp = processed_data[::]
            inp[1] = i
            inp[2] = j
            try:
                if find_first_num(inp) == 19690720:
                    return 100 * i + j
            except IndexError:
                continue
print(part2(inp))