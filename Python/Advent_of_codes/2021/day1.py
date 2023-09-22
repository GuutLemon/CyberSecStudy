with open('day1.txt') as f:
    read_data = f.read().strip().split('\n')
    int_data = [int(_) for _ in read_data]

    def check_increment(data):
        count = 0
        for d in range(1, len(data)):
            if data[d-1] < data[d]:
                count += 1
        return count

    # Part 1
    print(check_increment(int_data))

    # Part 2
    three_sum = [sum(int_data[i:i+3]) for i in range(len(read_data))]
    print(check_increment(three_sum))