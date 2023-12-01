with open("day2.txt") as f:
    read_data = f.read().strip().split('\n')
    processed_data = [[int(i) for i in j.split('\t')] for j in read_data]


def cal_checksum1(data):
    diff = []
    for line in data:
        diff.append(max(line) - min(line))
    return sum(diff)


print(cal_checksum1(processed_data))


def cal_checksum2(data):
    quotients = []
    for line in data:
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line)):
                if line[i] % line[j] == 0:
                    quotients.append(line[i] // line[j])
                elif line[j] % line[i] == 0:
                    quotients.append(line[j] // line[i])
    return sum(quotients)


print(cal_checksum2(processed_data))