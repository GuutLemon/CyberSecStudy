from itertools import product


def evaluate(equation, operators):
    result = 0
    value = equation[0]
    numbers = equation[1]
    op_combinatios = list(product(operators, repeat=len(numbers) - 1))
    for comb in op_combinatios:
        test = numbers[0]
        for i in range(len(numbers) - 1):
            if comb[i] == '+':
                test += numbers[i + 1]
            elif comb[i] == '*':
                test *= numbers[i + 1]
            else:
                concat = str(test) + str(numbers[i + 1])
                test = int(concat)
        if test == value:
            result += value
            break
    return result

def test_results(lst):
    result_1 = []
    result_2 = 0
    for line in lst:
        result_1.append(evaluate(line, {'+', '*'}))
    for line in lst:
        if line[0] not in result_1:
            result_2 += evaluate(line, {'+', '*', '||'})
    result_1 = sum(result_1)
    return result_1, result_2 + result_1


if __name__ == '__main__':
    with open('day07.txt') as f:
        INP = f.read().strip().split('\n')
        INP = [_.split(': ') for _ in INP]
        INP = [[int(i[0]), [int(j) for j in i[1].split()]] for i in INP]

    solve = test_results(INP)
    print('Part 1: ', solve[0])
    print('Part 2: ', solve[1])

