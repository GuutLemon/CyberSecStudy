with open('day3.txt') as f:
    read_data = f.read().strip().split('\n')
    #binaries = [int(i) for i in read_data]

    # Part 1
    def cal_powr(data):
        gamma = ''
        epsilon = ''
        count0 = 0
        count1 = 0
        for i in range(len(data[0])):
            for j in range(len(data)):
                if data[j][i] == '1':
                    count1 += 1
                else:
                    count0 += 1
            if max(count1, count0) == count1:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'
            count0 = 0
            count1 = 0   # 001101000100

        powr = int(gamma, 2) * int(epsilon, 2)
        return powr

    # Part 2
    def cal_ratings(data, min_max):
        check_bits = ''
        count0 = 0
        count1 = 0
        check_lst = data
        temp = []

        for i in range(len(data[0])):
            for j in range(len(check_lst)):
                if check_lst[j][i] == '1':
                    count1 += 1
                else:
                    count0 += 1

            if min_max == 'max':
                if max(count1, count0) == count1:
                    check_bits += '1'
                else:
                    check_bits += '0'
            else:
                if max(count1, count0) == count1:
                    check_bits += '0'
                else:
                    check_bits += '1'
            count0 = 0
            count1 = 0

            for j in range(len(check_lst)):
                if check_lst[j].startswith(check_bits):
                    temp.append(check_lst[j])
            #print(temp)
            if len(temp) == 1:
                return temp[0]
            check_lst = temp
            temp = []


    o2 = cal_ratings(read_data, 'max')
    co2 = cal_ratings(read_data, 'min')
    print(cal_powr(read_data))
    print(int(o2, 2) * int(co2, 2))

