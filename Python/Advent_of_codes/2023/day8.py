import math

with open('day8.txt') as f:
    read_data = f.read().strip().replace('(', '').replace(')', '').split('\n')

instructions = [0 if i == 'L' else 1 for i in read_data[0]]
network = {i.split(' = ')[0]: i.split(' = ')[1].split(', ') for i in read_data[2:]}


def count_steps(start):
    steps = 0
    current = start
    while current[-1] != 'Z':
        ins_indx = steps % len(instructions)
        current = network[current][instructions[ins_indx]]
        steps += 1
    else:
        return steps

print('Part 1:', count_steps('AAA'))


# Part 2
# Solved the same problem before but forgot which year it's in, the bus one
def find_factors(number):
    factors = []
    # Starts at 2 to not count 1 and itself
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    return factors

ends_with_A = [i for i in network if i[-1] == 'A']
steps_per_path = [count_steps(i) for i in ends_with_A]
factors_per_path = [find_factors(i) for i in steps_per_path]
# [[79, 263], [73, 263], [71, 263], [61, 263], [47, 263], [59, 263]]
# All paths end at the same time means finding a common factor for all these prime numbers and multiply it with 263
factors = set(i for j in factors_per_path for i in j)
print('Part 2:', math.prod(factors))
