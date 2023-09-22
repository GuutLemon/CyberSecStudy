#     # Part 1
# with open('day3.txt') as f:
#     read_data = f.read().strip()
#     visited_coords = [(0, 0)]
#     # Horizontal coord
#     x = 0
#     # Vertical coord
#     y = 0
#     #
#     for i in read_data:
#         if i == '>':
#             x += 1
#         elif i == '<':
#             x -= 1
#         elif i == '^':
#             y += 1
#         else:
#             y -= 1
#         visited_coords.append((x, y))
#     # Remove duplicated coords with set, the total number of coords remains should be the answer
#     print(len(set(visited_coords)))
#
#     ## Part 2
# with open('day3.txt') as f:
#     read_data = f.read().strip()
#     santa_visited_coords = [(0, 0)]
#     bot_visited_coords = [(0, 0)]
#     x = 0
#     y = 0
#
#     ## Get the moves of santa and bot
#     santa_move = ''
#     bot_move = ''
#     for i, j in enumerate(read_data):
#         if i % 2 == 0:
#             santa_move += j
#         else:
#             bot_move += j
#
#     ## Houses visited by Santa
#     for i in santa_move:
#         if i == '>':
#             x += 1
#         elif i == '<':
#             x -= 1
#         elif i == '^':
#             y += 1
#         else:
#             y -= 1
#         santa_visited_coords.append((x, y))
#     ## House visites by bot
#     ## Reset x and y
#     x = 0
#     y = 0
#     for i in bot_move:
#         if i == '>':
#             x += 1
#         elif i == '<':
#             x -= 1
#         elif i == '^':
#             y += 1
#         else:
#             y -= 1
#         bot_visited_coords.append((x, y))
#
#     visited_by_both = santa_visited_coords + bot_visited_coords
#     print(len(set(visited_by_both)))
#

# Redone
with open('day3.txt') as f:
    read_data = f.read().strip()


def moving(coord, d):
    directions = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    x, y = coord
    return x + directions[d][0], y + directions[d][1]


# Part 1
visited = set()
current = (0, 0)
for i in read_data:
    current = moving(current, i)
    visited.add(current)
print(len(visited))

# Part 2
visited = set()
san = (0, 0)
elf = (0, 0)
for i in range(len(read_data)):
    if i % 2 == 0:
        san = moving(san, read_data[i])
        visited.add(san)
    else:
        elf = moving(elf, read_data[i])
        visited.add(elf)
print(len(visited))