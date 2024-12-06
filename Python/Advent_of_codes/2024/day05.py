from collections import deque

def is_ordered(rules, check, i):
    if check[i] not in rules or all(check[j] not in rules[check[i]] for j in range(i + 1, len(check))):
        return check

def sort_order(rules, updates, corrects):
    fixed = []
    for u in updates:
        if u not in corrects:
            ordered = []
            check = deque(u)
            while len(ordered) < len(u):
                check.rotate(-1)
                if is_ordered(rules, check, 0):
                    ordered.append(check.popleft())
            fixed.append(ordered)
    return sum([f[len(f)//2] for f in fixed])

def solve(rules, updates):
    corrects = []
    for u in updates:
        check = u.copy()[::-1]
        if all(is_ordered(rules, check, page_indx) for page_indx in range(len(check))):
            corrects.append(u)
    fixed = sort_order(rules, updates, corrects)
    return sum([c[len(c)//2] for c in corrects]), fixed


if __name__ == '__main__':
    with open('day05.txt') as f:
        INP = f.read().strip().split('\n\n')
        pairs = [[int(i) for i in j.split('|')] for j in INP[0].split()]
        updates = [[int(i) for i in j.split(',')] for j in INP[1].split()]
        rules = {}
        for pair in pairs:
            if pair[0] not in rules:
                rules[pair[0]] = [pair[1]]
            else:
                rules[pair[0]].append(pair[1])

    result = solve(rules, updates)
    print('Part 1: ', result[0])
    print('Part 2: ', result[1])
