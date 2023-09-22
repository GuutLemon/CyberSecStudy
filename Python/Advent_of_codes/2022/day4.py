def check_contain(data):
    count1 = 0
    count2 = 0
    # Part 1
    for i in data:
        a, b, x, y = i
        if (a <= x and y >= b) or (x <= a and y >= b):
            count1 += 1

        # Part 2
        # Non-intersecting
        if (a < x and b < x) or (x < a and y < a):
            continue
        else:
            count2 += 1
    return count1, count2

with open('day4.txt') as f:
    read_data = f.read().strip().split('\n')
    # Group pairs and remove delimiters
    processed_data = [_.replace(',', '-') for _ in read_data]
    processed_data = [_.split('-') for _ in processed_data]
    processed_data = [[int(i) for i in j] for j in processed_data]
    # print(processed_data)
    print(check_contain(processed_data))