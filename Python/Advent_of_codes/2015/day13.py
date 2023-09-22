from itertools import permutations


# Just like day 9
def find_max_happiness(layouts, data):
    max_happiness = 0
    for seats in layouts:
        total_happiness = 0
        for i in range(len(seats)):
            if i < len(seats) - 1:
                total_happiness += data[(seats[i], seats[i-1])] + data[(seats[i], seats[i+1])]
            elif i == len(seats) - 1:
                total_happiness += data[(seats[i], seats[i - 1])] + data[(seats[i], seats[0])]
        if total_happiness > max_happiness:
            max_happiness = total_happiness
    return max_happiness


with open("day13.txt") as f:
    read_data = f.read().strip().split("\n")
    #print(read_data)
    processed_data = {}
    names = []

    for s in read_data:
        s = s.replace('would ', '').replace('happiness units by sitting next to ', '').replace('.', '').split()
        if s[1] == 'gain':
            processed_data[(s[0], s[-1])] = int(s[2])
        else:
            processed_data[(s[0], s[-1])] = -int(s[2])
        del s[1:-1]
        names.append(s)

    # Part 1
    names = list(set([i for j in names for i in j]))
    #print(names)
    #possible_seat_layouts = list(permutations(names))

    #print(find_max_happiness(possible_seat_layouts, processed_data))

    # Part 2
    for name in names:
        processed_data[('me', name)] = 0
        processed_data[(name, 'me')] = 0
    names.append('me')
    possible_seat_layouts = list(permutations(names))

    print(find_max_happiness(possible_seat_layouts, processed_data))