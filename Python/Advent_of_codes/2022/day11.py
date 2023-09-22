from pprint import pprint

def monkey_business(monkeys):
    # Part 2
    prime_mod = 1
    for monkey in monkeys.values():
        prime_mod *= monkey['div']
        # We only care about the monkeys test divisible numbers
        # The smallest number to divide is mod of multiplication of all of them
    ######

    inspect = []
    for round in range(10000):
        for monkey in monkeys.values():
            monkey['inspected'] += len(monkey['items'])
            #print(monkey['inspected'])
            for item in monkey['items']:
                if monkey['op'][-1] == 'old':
                    item = (item ** 2) % prime_mod       # // 3
                else:
                    item = eval(str(item) + ''.join(monkey['op'])) % prime_mod     # // 3
                if item % monkey['div'] == 0:
                    monkeys[str(monkey['true'])]['items'].append(item)
                else:
                    monkeys[str(monkey['false'])]['items'].append(item)
            monkey['items'] = []    # Don't use del because it will mess up the loop

    for monkey, value in monkeys.items():
        inspect.append({monkey: value['inspected']})
    return sorted(inspect, key=lambda x: list(x.values())[0], reverse=True)


with open('day11.txt') as f:
    read_data = f.read().strip().split('\n')
    monkeys = {}
    for l in range(0, len(read_data), 7):
        monkeys[read_data[l][-2]] = {}
        monkeys[read_data[l][-2]]['inspected'] = 0
        for i in read_data[l:l+7]:
            if i.startswith('  Start'):
                i = [j.split(', ') for j in i.split(': ')]
                i = [int(j) for j in i[1]]
                monkeys[read_data[l][-2]]['items'] = i
            elif i.startswith('  Oper'):
                i = i.split()[-2:]
                monkeys[read_data[l][-2]]['op'] = i
            elif i.startswith('  Test'):
                i = int(i.split()[-1])
                monkeys[read_data[l][-2]]['div'] = i
            elif i.startswith('    If true'):
                i = int(i.split()[-1])
                monkeys[read_data[l][-2]]['true'] = i
            elif i.startswith('    If false'):
                i = int(i.split()[-1])
                monkeys[read_data[l][-2]]['false'] = i

    pprint(monkeys)

    inspect = monkey_business(monkeys)
    print(inspect)
