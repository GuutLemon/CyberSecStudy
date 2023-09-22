inp = [0, 14, 6, 20, 1, 4]
# inp = [0, 3, 6]

most_recent_num = inp[-1]

# Part 1
# for i in range(len(inp) - 1, 2019):
#     if most_recent_num in inp[:-1]:
#         most_recent_indx = len(inp) - 2 - inp[:-1][::-1].index(most_recent_num)
#         most_recent_num = i - most_recent_indx
#         inp.append(most_recent_num)
#     else:
#         inp.append(0)
#         most_recent_num = 0
# print(inp[-1])

# Part 2
# dict is much faster but a lot more tricky
num_pos = {}
for i in range(len(inp) - 1):
    num_pos[inp[i]] = i
print(num_pos)  # Mark position of every numbers in inp[:-1]

# i will always equal the max index of inp (len(inp)-1), so the loop starts at inp[-1] and most_recent_num = inp[-1]
# most_recent_num -> NEW most_recent_num -> track the closest NEW most_recent_num -> update or add position of NEW most_recent_num to num_pos -> repeat
for i in range(len(inp) - 1, 30000000-1):
    # Second loop and the rest starts here
    if most_recent_num in num_pos:
        # 0 is not a new number so most_recent_num will be max index minuses index of the nearest 0 which is tracked in the first loop
        most_recent_num = i - previous_num_indx
        # Keep track of the nearest NEW most_recent_num before updating its new position
        if most_recent_num in num_pos:
            previous_num_indx = num_pos[most_recent_num]
        else:   # New number, track itself
            previous_num_indx = i + 1
        # Update new position
        num_pos[most_recent_num] = i + 1
        # print(i, most_recent_num)

    # First loop starts here, inp[:-1] not in inp
    # This will run only once to jump start
    else:
        # Add the new number and its position
        num_pos[most_recent_num] = i
        most_recent_num = 0
        # Keep track of the old 0 which is the NEW most_recent_num
        previous_num_indx = num_pos[0]
        # Update the old 0 position to the new 0. Since it will be added behind the largest index of inp, it will be i + 1
        num_pos[most_recent_num] = i + 1
        # print('B', previous_num_indx)
    # print(num_pos)

print(most_recent_num)


