def check_order(signals):
    print(signals)
    if all(isinstance(s, int) for s in signals):
        if signals[1] > signals[0]:
            return 1
        elif signals[1] == signals[0]:
            return 0
        return -1

    # Convert both values to list if one is list
    elif not all(isinstance(s, int) for s in signals):
        signals = [[s] if isinstance(s, int) else s for s in signals]

    min_length = min(len(signals[0]), len(signals[1]))
    # if min_length == 0 == len(signals[0]):
    #     return 1
    # elif min_length == 0 == len(signals[1]):
    #     return -1
    x = 0
    for i in range(min_length):
        print([signals[0][i], signals[1][i]])
        x = check_order([signals[0][i], signals[1][i]])

        print(x)
        if x == 1:
            return 1
        elif x == -1:
            return -1
    if x == 0:
        print('min', min_length, len(signals[1]))
        if min_length == len(signals[0]):
            return 1
        elif min_length == len(signals[1]):
            return -1
        elif len(signals[0]) == len(signals[1]):
            return -1



with open('day12.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = []
    # Group pairs and turn them to actual lists
    for i in range(0, len(read_data), 3):
        processed_data.append([eval(read_data[i]), eval(read_data[i+1])])

    check = []
    for i, j in enumerate(processed_data):
        print(j, check_order(j))
        if check_order(j) == 1:
            check.append(i+1)
    print(sum(check))

