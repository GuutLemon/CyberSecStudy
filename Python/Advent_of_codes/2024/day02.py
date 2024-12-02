def check_levels(lst):
    safe_1 = 0
    safe_2 = 0
    for l in lst:
        decre = 0
        incre = 0
        for i in range(len(l) - 1):
            if -3 <= l[i] - l[i+1] <= -1:
                incre += 1
            elif 1 <= l[i] - l[i+1] <= 3:
                decre += 1
        if incre == len(l) - 1 or decre == len(l) - 1:
            safe_1 += 1
            safe_2 += 1
        else:
            for i in range(len(l)):
                test = l[:i] + l[i+1:]
                if all(-3 <= test[j] - test[j+1] <= -1 for j in range(len(test) - 1))\
                        or all(1 <= test[j] - test[j+1] <= 3 for j in range(len(test) - 1)):
                    safe_2 += 1
                    break
    return safe_1, safe_2


if __name__ == '__main__':
    with open('day02.txt') as f:
        INP = f.read().strip().split('\n')
        INP = [[int(i) for i in j.split()] for j in INP]

    solve = check_levels(INP)
    print('Part 1: ', solve[0])
    print('Part 2: ', solve[1])