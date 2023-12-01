with open("day1.txt") as f:
    read_data = f.read().strip().split('\n')

num_lists = [[i for i in j if i.isdigit()] for j in read_data]

values = []
for l in num_lists:
    if len(l) == 1:
        values.append(int(l[0]*2))
    elif len(l) != 0:
        values.append(int(l[0] + l[-1]))
print("Part 1:", sum(values))


# Part 2
values = []

# def line_check(line):
#     word_nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
#                  'nine': '9'}
#     # print(line)
#     if len(line) == 1:
#         if line.isdigit():
#             yield line
#             return
#         else:
#             return
#     elif len(line) == 0:
#         return
#
#     check = ''
#     for i, j in enumerate(line):
#         check += j
#         if i == 0 and j.isdigit():
#             line = line[i + 1:]
#             yield j
#             break
#         elif i < 5:
#             if check in word_nums:
#                 line = line[i:]
#                 yield word_nums[check]
#                 break
#             elif i == len(line) - 1:
#                 line = line[1:]
#                 break
#         else:
#             line = line[1:]
#             break
#     yield from line_check(line)

# Cleaner ver
def line_check(line):
    word_nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                  'nine': '9'}
    # print(line)
    if len(line) == 0:
        return
    if line[0].isdigit():
        yield line[0]
        line = line[1:]
    elif line[:3] in word_nums:
        yield word_nums[line[:3]]
        line = line[2:]
    elif line[:4] in word_nums:
        yield word_nums[line[:4]]
        line = line[3:]
    elif line[:5] in word_nums:
        yield word_nums[line[:5]]
        line = line[4:]
    else:
        line = line[1:]
    yield from line_check(line)


for l in read_data:
    result = list(line_check(l))
    if len(result) == 1:
        values.append(int(result[0] * 2))
    else:
        values.append(int(result[0] + result[-1]))
    # print(result, values)
print("Part 2:", sum(values))