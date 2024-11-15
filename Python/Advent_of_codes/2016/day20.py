def merge_couple(r1, r2):
    if (r1[0] > r2[0] and r1[0] > r2[1] + 1) or (r1[1] + 1 < r2[0] and r1[1] + 1 < r2[1]):
        return [r1, r2]
    if r1[0] < r2[0]:
        if r1[1] < r2[1]:
            return r1[0], r2[1]
        else:
            return r1
    if r1[0] > r2[0]:
        if r1[1] > r2[1]:
            return r2[0], r1[1]
        else:
            return r2

def full_merge(lst):
    result = []
    leftover_ranges = sorted(lst, key=lambda r: r[0])
    while leftover_ranges:
        new_leftover_ranges = []
        current_range = leftover_ranges[0]
        for r in leftover_ranges[1:]:
            merged = merge_couple(current_range, r)
            if isinstance(merged, list):
                new_leftover_ranges.append(merged[1])
                current_range = merged[0]
            else:
                current_range = merged
        leftover_ranges = new_leftover_ranges.copy()
        result.append(current_range)
    return result

def get_lowest_allowed(lst):
    min_range = sorted(lst, key=lambda r: r[0])
    return min_range[0][1] + 1

def count_allowed(lst):
    max_ip = 4294967295
    count = 0
    l = len(lst)
    for i in range(l):
        if i == l - 1:
            if lst[i][1] < max_ip:
                count += max_ip - (lst[i][1] + 1)
        else:
            count += lst[i+1][0] - (lst[i][1] + 1)
    return count


if __name__ == '__main__':
    with open('day20.txt') as f:
        ranges = f.read().strip().split('\n')
        ranges = [tuple(int(i) for i in j.split('-')) for j in ranges]
        merged_ranges = full_merge(ranges)
        print('Part 1: ', get_lowest_allowed(merged_ranges))
        print('Part 2: ', count_allowed(merged_ranges))
