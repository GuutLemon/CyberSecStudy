def group_column(inp):
    grouped = []
    for i in range(len(inp[0])):
        column = ''
        for j in range(len(inp)):
            column += inp[j][i]
        grouped.append(column)
    return grouped

def find_common_char(string, sort=0):
    count = {}
    for char in string:
        if char not in count:
            count[char] = string.count(char)
    if sort == 0:
        sorted_count = sorted(count.items(), key=lambda items: -items[1])
    else:
        sorted_count = sorted(count.items(), key=lambda items: items[1])
    return sorted_count[0][0]


def find_message(sig, part=1):
    message = ''
    for s in sig:
        if part == 1:
            char = find_common_char(s, 0)
        elif part == 2:
            char = find_common_char(s, 1)
        message += char
    return message

if __name__ == '__main__':
    with open('day6.txt') as f:
        signals = f.read().strip().split('\n')
        signals = group_column(signals)
    print('Part 1: ', find_message(signals, 1))
    print('Part 2: ', find_message(signals, 2))

