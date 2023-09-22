def count_combinations(containers, total_liters, min=0, min_combs=[]):
    if total_liters == 0:
        min += 1
        min_combs.append(min)
        min = 0
        return 1, min, min_combs
    if total_liters > 0:
        min += 1
    if total_liters < 0 or not containers:
        min = 0
        return 0, min, min_combs

    # Count combinations including the current container
    count_incl = count_combinations(containers[1:], total_liters - containers[0], min, min_combs)

    # Count combinations excluding the current container
    count_excl = count_combinations(containers[1:], total_liters, 0, min_combs)

    return count_incl[0] + count_excl[0], min, min_combs


with open("day17.txt") as f:
    read_data = f.read().strip().split("\n")
    sorted = sorted([int(i) for i in read_data], reverse=True)
    total = 150
    print(sorted)
    result, _, mincomb = count_combinations(sorted, total)
    print(mincomb)
    min = min(mincomb)
    print(min)
    print(mincomb.count(min))
