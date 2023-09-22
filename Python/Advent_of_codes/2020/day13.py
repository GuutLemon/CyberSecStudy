with open('day13.txt') as f:
    read_data = f.read().strip().split('\n')
    start_wait = int(read_data[0])
    buses = [int(i) if i.isdigit() else i for i in read_data[1].split(',')]
    active_buses = [i for i in buses if isinstance(i, int)]


# Part 1
def cal_wait_time(start, lst):
    for i in range(start, start + max(lst)):
        for b in lst:
            if i % b == 0:
                return (i - start)*b

print(cal_wait_time(start_wait, active_buses))


# Part 2
def find_timestamp(buses, active_buses):
    # b_indx = {}
    # maxb = max(active_buses)
    # maxb_indx = buses.index(maxb)
    # for b in range(len(buses)):
    #     if buses[b] != 'x':
    #         b_indx[b - maxb_indx] = buses[b]
    #
    # i = 100000000000000 - (100000000000000 % maxb)
    # while True:
    #     i += maxb
    #     # print(i)
    #     if all((i + j) % b_indx[j] == 0 for j in b_indx):
    #         return i + list(b_indx.keys())[0]
    # Not fast enough

    # Had to google
    b_indx = []
    for b in range(len(buses)):
        if buses[b] != 'x':
            b_indx.append(b)

    i = 0
    step = active_buses[0]
    for b in range(len(b_indx) - 1):
        while True:
            if (i + b_indx[b+1]) % active_buses[b+1] == 0:
                step *= active_buses[b+1]
                break
            i += step
    return i

print(find_timestamp(buses, active_buses))
