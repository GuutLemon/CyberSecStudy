with open('day6.txt') as f:
    read_data = f.read().strip().split('\n')

time = [int(_) for _ in read_data[0].split(':')[1].split()]
dist = [int(_) for _ in read_data[1].split(':')[1].split()]

def make_moves(t: int):
    max_dist = []
    for hold_time in range(1, t):
        max_dist.append(hold_time * (t - hold_time))
    return max_dist

total_beats = 1
for t in range(len(time)):
    beat = 0
    moves = make_moves(time[t])
    for m in moves:
        if m > dist[t]:
            beat += 1
    total_beats *= beat
print(total_beats)


# Part 2
time = int("".join(read_data[0].split(':')[1].split()))
dist = int("".join(read_data[1].split(':')[1].split()))

def find_start_beating_index(range_check: tuple, t: int ,d: int):
    for i in range(1, 6):
        hold_time = (max(range_check) - min(range_check)) // 5 * i
        max_dist = hold_time * (t - hold_time)
        if max_dist > d:
            # (previous hold time, hold time)
            new_range = ((max(range_check) - min(range_check)) // 5 * (i - 1), hold_time)
            return find_start_beating_index(new_range, t, d)
    # Last check, smallest range
    for i in range(min(range_check), max(range_check) + 1):
        max_dist = i * (t - i)
        if max_dist > d:
            return len(range(i, (t - i) + 1))

print(find_start_beating_index((1, time - 1), time, dist))
