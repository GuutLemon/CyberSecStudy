def sum_priorities(data):
    priorities_lst = []
    sum = 0
    for i in data:
        # Set operation
        # Part 1
        #priorities_lst.append(list(set(i[0]) & set(i[1]))[0])
        # Part 2
        priorities_lst.append(list(set(i[0]) & set(i[1]) & set(i[2]))[0])
    print(priorities_lst)
    for p in priorities_lst:
        #print(p)
        if p.isupper():
            p = ord(p.lower()) - ord('a') + 1 + 26
        else:
            p = ord(p) - ord('a') + 1
        #print(p)
        sum += p
    return sum



with open('day3.txt') as f:
    read_data = f.read().strip().split('\n')
    print(read_data)
    # Part 1
    # processed_data = []
    # for l in read_data:
    #     half_index = len(l) // 2
    #     l = [list(l[:half_index]), list(l[half_index:])]
    #     processed_data.append(l)
    # #print(processed_data)
    # print(sum_priorities(processed_data))

    # Part 2
    processed_data = [[list(i) for i in read_data[j:j+3]] for j in range(0, len(read_data), 3)]
    print(processed_data)
    print(sum_priorities(processed_data))