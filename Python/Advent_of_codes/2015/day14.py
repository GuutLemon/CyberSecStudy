def cal_distance(speed, limit, recover, time):
    distance = 0
    sustaining = True
    sustaining_time = 0
    resting = False
    resting_time = 0
    for i in range(1, time + 1):    # range(time + 1) only will not work. Time starts at 1, not 0
        if sustaining:
            distance += speed
            sustaining_time += 1
            if sustaining_time == limit:
                sustaining = False
                sustaining_time = 0
                resting = True
        elif resting:
            resting_time += 1
            if resting_time == recover:
                resting = False
                resting_time = 0
                sustaining = True
    return distance


with open("day14.txt") as f:
    read_data = f.read().strip().split("\n")
    processed_data = {}
    for s in read_data:
        s = s.split()
        processed_data[s[0]] = [int(i) for i in s if i.isdigit()]

    # Part1
    # all_distances = []
    # for key in processed_data.keys():
    #     all_distances.append(cal_distance(*processed_data[key], 2503))
    # print(max(all_distances))

    # Part 2
    personal_distances = {}
    personal_scores = {key: 0 for key in processed_data.keys()}
    for i in range(1, 2503 + 1):
        for key in processed_data:
            personal_distances[key] = cal_distance(*processed_data[key], i)
            #print(personal_distances[key])
        current_max_distance = max(personal_distances.values())
        for key in personal_distances:
            if personal_distances[key] == current_max_distance:
                personal_scores[key] += 1

    print(max(personal_scores.values()))
