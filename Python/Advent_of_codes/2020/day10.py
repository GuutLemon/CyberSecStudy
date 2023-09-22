# import itertools

with open('day10.txt') as f:
    read_data = f.read().strip().split('\n')
    adapters = [int(_) for _ in read_data]
    adapters.sort()
    adapters.append(max(adapters) + 3)      # Add device
    adapters.insert(0, 0)   # Add outlet
    print(adapters)

# Part 1
count1 = 0
count3 = 0
for i in range(1, len(adapters)):
    if adapters[i] - adapters[i-1] == 1:
        count1 += 1
    elif adapters[i] - adapters[i-1] == 3:
        count3 += 1

print(count1, count3, count1 * count3)


# Part 2
# Had to google
def find_arrangements(lst, indx=0, recur_mem={}):
    if indx in recur_mem:
        return recur_mem[indx]

    if indx == len(lst) - 1:
        return 1

    count = 0
    for i in range(1, 4):
        if indx + i < len(lst) and lst[indx+i] - lst[indx] <= 3:
            count += find_arrangements(lst, indx+i, recur_mem)

    recur_mem[indx] = count
    return count


print(find_arrangements(adapters))




