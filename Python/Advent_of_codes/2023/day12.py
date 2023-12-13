with open('day12.txt') as f:
    read_data = f.read().strip().split('\n')

spr_rows = tuple(i.split()[0] for i in read_data)
dmg_groups = tuple(tuple(map(int, i.split()[1].split(','))) for i in read_data)

# Had to watch walkthrough
cache = {}
def count_arrangements(row, group):
    count = 0
    key = (row, group)
    if key in cache:
        return cache[key]
    # Early break
    if len(row) < sum(group) + len(group) - 1:
        return 0
    # Check at the end
    if not row:
        return 1 if not group else 0
    if not group:
        return 0 if '#' in row else 1
    # Don't have to do  for s in '.#'
    if row[0] in '.?':
        count += count_arrangements(row[1:], group)
    if row[0] in '#?':
        # ('#?#?', (4)) or ('#?#?....', (4, 3))
        if '.' not in row[:group[0]] and (len(row) == group[0] or row[group[0]] != '#'):
            # Jump right to next group #?#?.|...
            count += count_arrangements(row[group[0] + 1:], group[1:])
    cache[key] = count
    return count

total_1 = 0
total_2 = 0
for i in range(len(read_data)):
    total_1 += count_arrangements(spr_rows[i], dmg_groups[i])
    g = dmg_groups[i] * 5
    s = '?'.join([spr_rows[i]] * 5)
    total_2 += count_arrangements(s, g)
print(total_1)
print(total_2)