with open('day5.txt') as f:
    read_data = f.read().strip().split('\n\n')
    seed_map = [i.strip().split('\n') for j in read_data for i in j.split(':')[1:]]
    seed_map = [[[int(i) for i in j.split()] for j in k] for k in seed_map]


def make_ranges():
    props = []
    for prop in seed_map[1:]:
        ranges = []
        for line in prop:
            ranges.append([(range(line[1], line[1] + line[2]), range(line[0], line[0] + line[2]))])
        props.append(ranges)
    return props


seeds = seed_map[0][0]
properties = make_ranges()
print(properties)


def mapping(n, i=0):
    if i > len(properties) - 1:
        return n
    for line in properties[i]:
        for r in line:
            if n in r[0]:
                n = r[1][n - r[0][0]]
                i += 1
                return mapping(n, i)
    i += 1
    return mapping(n, i)


mapped_loc = set()
for s in seeds:
    mapped_loc.add(mapping(s))
print(min(mapped_loc))


# Part 2
seeds2 = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
# print(seeds2)

# Crashed
# def mapping2(rn, i=0):
#     # print(rn)
#     if i > len(properties) - 1:
#         return min(rn)
#       mapped = set()
#     not_in_range = []
#     for line in properties[i]:
#         for r in line:
#             in_range = rn & set(r[0])
#             not_in_range.append(rn - in_range)
#             if in_range:
#                 mapped |= set(range(min(in_range) - (r[0][0] - r[1][0]), max(in_range) + 1 - (r[0][0] - r[1][0])))
#     not_in_range = set(set.intersection(*not_in_range))
#     mapped |= not_in_range
#     i += 1
#     return mapping2(mapped, i)      # Stuck for 1 hour because return mapping instead of mapping2
#                                     # Next time name mapping_part 2 or something more obvious


def mapping_part2(ranges: list, i=0):
    print(ranges)
    if i > len(properties) - 1:
        return ranges
    next_ranges = []
    for p in properties[i]:
        for rn in ranges:
            for r in p:
                s, e = rn[0], rn[1]
                overlapped_s = max(s, r[0].start)
                overlapped_e = min(e, r[0].stop)
                if overlapped_s < overlapped_e:
                    next_ranges.append((overlapped_s + r[1][0] - r[0][0], overlapped_e + r[1][0] - r[0][0]))
                    # Not matched
                    if overlapped_s > s:
                        next_ranges.append((s, overlapped_s))
                    if overlapped_e < e:
                        next_ranges.append((overlapped_e, e))
            if rn == ranges[-1:]:
                i += 1
                return mapping_part2(next_ranges, i)

        i += 1
        return mapping_part2(ranges, i)


mapped_loc = []
for s in seeds2:
    mapped_loc.append(mapping_part2([s]))
results = [i for j in mapped_loc for i in j]
print(results)
print(sorted(results, key=lambda x: x[0])[0][0])