import re


def check_prop(data):
    # Part 1
    # lines = [
    #     'children: 3',
    #     'cats: 7',
    #     'samoyeds: 2',
    #     'pomeranians: 3',
    #     'akitas: 0',
    #     'vizslas: 0',
    #     'goldfish: 5',
    #     'trees: 3',
    #     'cars: 2',
    #     'perfumes: 1',
    # ]

    # Part 2
    lines = [
        'children: 3',
        'cats: ([8-9]{1},|\d\d,)',
        'samoyeds: 2',
        'pomeranians: [0-2]{1},',
        'akitas: 0',
        'vizslas: 0',
        'goldfish: [0-4]{1},',
        'trees: ([4-9]{1},|\d\d,)',
        'cars: 2',
        'perfumes: 1',
    ]
    result = []
    for i in data:
        check = 0
        for j in lines:
            if re.search(j, i):
                check += 1
                print(re.search(j, i))
        if check == 3:
            result.append(i)
    return result


with open("day16.txt") as f:
    read_data = f.read().strip().split("\n")
    # aunts = {}
    # for i in read_data:
    #     i = i.replace(', ', ': ').split(": ")
    #     aunts[i[0]] = {i[1:][j]: int(i[1:][j + 1]) for j in range(0, len(i[1:]), 2)}

    print(check_prop(read_data))