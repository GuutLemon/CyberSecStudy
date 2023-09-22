with open('day1.txt') as f:
    read_data = f.read().strip().split('\n')
    nums = [int(_) for _ in read_data]

    # Part 1
    for i in nums:
        if 2020 - i in nums:
            print(i * (2020 - i))
            break

    # Part 2
    for i in nums:
        for j in nums:
            k = 2020 - j - i
            if k in nums:
                print(i * j * k)
                k = -1
                break
        if k == -1:
            break