with open('day5.txt') as f:
    read_data = f.read().strip()
    processed_data = eval('[' + read_data + ']')


code = processed_data[::]
# inp = 5
inp = [5]
def intcode(code, inp):
    i = 0
    # op_list = ['1', '2', '3', '4', '5', '6', '7', '8']
    while code[i] != 99:
        op = str(code[i])[-1]
        # Assuming 000x
        param_1 = 'code[code[i + 1]]'
        param_2 = 'code[code[i + 2]]'
        param_3 = 'code[code[i + 3]]'
        # Then check
        if (code[i] // 100) % 10 == 1:
            param_1 = 'code[i + 1]'
        if (code[i] // 1000) % 10 == 1:
            param_2 = 'code[i + 2]'
        if (code[i] // 10000) % 10 == 1:
            param_3 = 'code[i + 3]'

        if op == '1':
            exec(f'{param_3} = {param_1} + {param_2}')
            i += 4
        elif op == '2':
            exec(f'{param_3} = {param_1} * {param_2}')
            i += 4
        elif op == '3':
            # exec(f'{param_1} = inp')
            # Change for day7
            if i == 0:
                exec(f'{param_1} = inp[0]')
            elif len(inp) > 1:
                exec(f'{param_1} = inp[1]')
            ############
            i += 2
        elif op == '4':
            yield eval(param_1)
            i += 2

        # Part 2
        elif op == '5':
            if eval(param_1) != 0:
                i = eval(param_2)
            else:
                i += 3
        elif op == '6':
            if eval(param_1) == 0:
                i = eval(param_2)
            else:
                i += 3
        elif op == '7':
            if eval(param_1) < eval(param_2):
                exec(f'{param_3} = 1')
            else:
                exec(f'{param_3} = 0')
            i += 4
        elif op == '8':
            if eval(param_1) == eval(param_2):
                exec(f'{param_3} = 1')
            else:
                exec(f'{param_3} = 0')
            i += 4


if __name__ == '__main__':
    for i in intcode(code, inp):
        print(i)
