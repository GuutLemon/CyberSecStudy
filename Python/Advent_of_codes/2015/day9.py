from itertools import permutations


def distance_cal(paths, distances):
    min_total_distance = 99999999999999999999
    max_total_distance = 0
    for i in paths:
        total_distance = 0
        for j in range(len(i)):
            if j < len(i) - 1:
                if (i[j], i[j+1]) in distances:
                    total_distance += distances[(i[j], i[j+1])]
                else:
                    total_distance = 0
                    break
        # Part 1
        if total_distance < min_total_distance and total_distance != 0:
            min_total_distance = total_distance
        # Part 2
        if total_distance > max_total_distance:
            max_total_distance = total_distance

    return min_total_distance, max_total_distance

with open("day9.txt") as f:
    read_data = f.read().strip().split("\n")
    processed_dara = [i.replace("to ", "").replace("= ", "").split() for i in read_data]

    # Making a dictionary for patch and distance using " = " as delimiter, INCLUDING REVERSED PATHS
    distances = {(place1, place2): int(distance) for i in processed_dara for place1, place2, distance in [i]}
    distances.update({(place2, place1): int(distance) for i in processed_dara for distance, place2, place1 in [i[::-1]]})

    # Making a set of unique places
    [i.remove(i[-1]) for i in processed_dara]
    places = list(set([i for j in processed_dara for i in j]))

    # Find all possible paths to calculate distances
    possible_paths = list(permutations(places))
    print(distance_cal(possible_paths, distances))

