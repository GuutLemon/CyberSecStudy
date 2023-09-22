with open('day8.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [[i.split() for i in j.split(' | ')] for j in read_data]
    sigs = [i[0] for i in processed_data]
    outs = [i[1] for i in processed_data]

    # Part 1
    # valid_outs_len = [2, 4, 3, 7]
    # count = 0
    # for i in processed_data:
    #     for outs in i[1]:
    #         if len(outs) in valid_outs_len:
    #             count += 1
    # print(count)

    # Part 2
    display = []
    num = {}
    num['len5'] = []
    num['len6'] = []

    for i in sigs:
        for s in i:
            if len(s) == 2:
                num['1'] = set(s)
            elif len(s) == 4:
                num['4'] = set(s)
            elif len(s) == 3:
                num['7'] = set(s)
            elif len(s) == 7:
                num['8'] = set(s)
            elif len(s) == 5:
                num['len5'].append(set(s))
            elif len(s) == 6:
                num['len6'].append(set(s))

        # Brute force
        for n in num['len6']:
            u = num['1'] | num['4'] | num['7']
            if len(list(n | num['1'])) == 7:
                num['6'] = n
            elif len(list(n - u)) == 1:
                num['9'] = n
            else:
                num['0'] = n

        for n in num['len5']:
            if len(list(num['6'] - n)) == 1:
                num['5'] = n
            elif len(list(num['9'] - n)) == 1:
                num['3'] = n
            else:
                num['2'] = n
        display.append(num)
        num = {}
        num['len5'] = []
        num['len6'] = []

    num = ''
    all_nums = []
    for i, j in enumerate(outs):
        for o in j:
            for s, v in display[i].items():
                if set(o) == v:
                    #print(o, v)
                    num += s
        all_nums.append(int(num))
        num = ''

    print(sum(all_nums))