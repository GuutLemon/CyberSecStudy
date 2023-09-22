import copy

with open('day2.txt') as f:
    read_data = f.read().strip().split('\n')
    # Create a list of lists of cubes dimensions
    # Turn data into int
    processed_data = [[int(j) for j in k] for k in [i.split('x') for i in read_data]]
    # Part 1
    sum_paper = 0
    # Create a list of smallest sides
    smallest_sides = copy.deepcopy(processed_data)
    [i.remove(max(i)) for i in smallest_sides]
    # Surface of cube + smallest surface of cube
    for j, i in enumerate(processed_data):
        sum_paper += 2 * i[0] * i[1] + 2 * i[1] * i[2] + 2 * i[0] * i[2]
        sum_paper += smallest_sides[j][0] * smallest_sides[j][1]
    print(sum_paper)

    # Part 2
    sum_ribbon = 0
    for j, i in enumerate(smallest_sides):
        sum_ribbon += (i[0] + i[1]) * 2
        sum_ribbon += processed_data[j][0] * processed_data[j][1] * processed_data[j][2]
    print(sum_ribbon)