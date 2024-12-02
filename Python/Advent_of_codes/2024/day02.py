def verify_safety(lst):
    diff = set(lst[i + 1] - lst[i] for i in range(len(lst) - 1))
    return diff <= {1, 2, 3} or diff <= {-1, -2, -3}

def check_levels(lst):
    safe_1 = 0
    safe_2 = 0
    for l in lst:
        if verify_safety(l):
            safe_1 += 1
            safe_2 += 1
        else:
            for i in range(len(l)):
                test = l[:i] + l[i+1:]
                if verify_safety(test):
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