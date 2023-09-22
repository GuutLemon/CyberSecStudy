with open('day5.txt') as f:
    read_data = f.read().strip()

char_list = set(map(chr, range(ord('a'), ord('z')+1)))
check_list = set([i.upper() + i for i in char_list] + [i + i.upper() for i in char_list])
check_list2 = set([(i, i.upper()) for i in char_list])
print(check_list)
print(check_list2)


def shortening(data):
    while True:
        if all(check not in data for check in check_list):
            return len(data)
        for check in check_list:
            if check in data:
                data = data.replace(check, '')


# Part 1
print(shortening(read_data))

# Part 2
lens = set()
for i in check_list2:
    test = read_data
    for j in i:
        test = test.replace(j, '')
    lens.add(shortening(test))

print(min(lens))