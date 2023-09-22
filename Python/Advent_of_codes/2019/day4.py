inp = '130254-678275'
inp = [int(_) for _ in inp.split('-')]


def valid(passwd):
    same_adja = False
    not_decreasing = True

    for i in range(len(passwd) - 1):
        if passwd[i] == passwd[i + 1]:
            same_adja = True
        if passwd[i + 1] < passwd[i]:
            not_decreasing = False

    # Part 2
    only_2 = 2 in [passwd.count(i) for i in passwd]

    if same_adja and not_decreasing and only_2:
        return True


def count_valid(inp):
    valids = []
    for i in range(inp[0], inp[1] + 1):
        if valid(str(i)):
            valids.append(i)
    return len(valids)


print(count_valid(inp))