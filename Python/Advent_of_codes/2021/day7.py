with open('day7.txt') as f:
    read_data = f.read().strip()
    pos = eval('[' + read_data + ']')

    def cal_fuel(x, y):
        result = 0
        a = min(x, y)
        b = max(x, y)
        for i in range(b - a):
            result += i + 1
            #print(result)
        return result

    total_fuel = []
    current_fuel = []
    for i in range(max(pos) + 1):
        for j in pos:
            # Part 1
            # current_fuel.append(abs(i - j))
            # Part 2
            current_fuel.append(cal_fuel(i, j))
        #print(current_fuel)
        total_fuel.append(sum(current_fuel))
        current_fuel = []

    print(min(total_fuel))