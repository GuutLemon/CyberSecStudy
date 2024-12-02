def solve1(lst_1, lst_2):
    lst_1 = sorted(lst_1)
    lst_2 = sorted(lst_2)
    result = 0
    l = len(lst_1)
    for i in range(l):
        result += abs(lst_1[i] - lst_2[i])
    return result

def solve2(lst_1, lst_2):
    result = 0
    l = len(lst_1)
    for i in range(l):
        result += lst_1[i] * lst_2.count(lst_1[i])
    return result


if __name__ == '__main__':
    with open('day01.txt') as f:
        INP = f.read().strip().split('\n')

    LST_1 = []
    LST_2 = []
    for n in INP:
        n = n.split()
        LST_1.append(int(n[0]))
        LST_2.append(int(n[1]))

    print('Part 1: ', solve1(LST_1, LST_2))
    print('Part 2: ', solve2(LST_1, LST_2))