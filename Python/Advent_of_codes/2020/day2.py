with open('day2.txt') as f:
    read_data = f.read().strip().replace(':', '').replace('-', ' ').split('\n')
    processed_data = [[int(i) if i.isdigit() else i for i in j.split(' ')] for j in read_data]

    count1 = 0
    count2 = 0
    for p in processed_data:
        # Part 1
        r = range(p[0], p[1] + 1)
        char = p[2]
        if p[3].count(char) in r:
            count1 += 1

        # Part 2
        start = p[0]-1
        end = p[1]-1
        try:
            if (p[3][start] == char or p[3][end] == char) and p[3][start] != p[3][end]:
                count2 += 1
        except IndexError:
            continue

    print(count1)
    print(count2)
