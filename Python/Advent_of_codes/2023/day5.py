with open('day5.txt') as f:
    read_data = f.read().strip().split('\n\n')
    seed_map = [i.strip().split('\n') for j in read_data for i in j.split(':')[1:]]
    seed_map = [[[int(i) for i in j.split()] for j in k] for k in seed_map]


def make_to_map():
    props = []
    for prop in seed_map[1:]:
        to_map = []
        for line in prop:
            to_map.append((range(line[1], line[1] + line[2]), range(line[0], line[0] + line[2])))
        props.append(to_map)
    return props


seeds = seed_map[0][0]
properties = make_to_map()
print(properties)


def mapping(n, i=0):
    if i > len(properties) - 1:
        return n
    for r in properties[i]:
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

# Too slow and crashing
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


def mapping_part2(to_map: list):
    for p in properties:
        next = []
        # for tm in to_map:
        while len(to_map) > 0:
            # print(to_map)
            s, e = to_map.pop()
            # print(to_map)
            # Remove mapped
            # to_map.remove(tm)
            for r in p:
                overlapped_s = max(s, r[0].start)
                overlapped_e = min(e, r[0].stop)
                if overlapped_s < overlapped_e:
                    next.append((overlapped_s + r[1][0] - r[0][0], overlapped_e + r[1][0] - r[0][0]))
                    # Not overlapped part, add to mapping loop
                    if overlapped_s > s:
                        to_map.append((s, overlapped_s))
                    if overlapped_e < e:
                        to_map.append((overlapped_e, e))
                    break
            else:       # "else block is executed when the while loop condition becomes False."
                        # So while len(to_map) > 0 always run at least twice because first loop is not False
            # if len(to_map) == 0:  # while len(to_map) > 0 only runs once because the if line rechecks its condition -> wrong results
            #     print('A')
                next.append((s, e))
                # print('B', next)      # Leaving debug lines for future revisits
        to_map = next[:]
    return to_map

mapped_loc = []
for s in seeds2:
    mapped_loc.append(mapping_part2([s]))
results = [i for j in mapped_loc for i in j]
print(results)
print(min(results))
