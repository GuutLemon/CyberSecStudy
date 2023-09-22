# def check_visible(data):
#     length = len(data) - 1
#     scenic_scores = []
#     #visible_count = len(data) * 4 - 4
#     for y_index, row in enumerate(data):
#         for x_index, tree in enumerate(row):
#
#             # Part 1
#             # Excluding outer trees
#             # if 0 < x_index < length and 0 < y_index < length:
#             #     # Check in 4 directions
#             #     w_visible = True
#             #     e_visible = True
#             #     n_visible = True
#             #     s_visible = True
#             #
#             #     for other_tree_index in range(length + 1):
#             #         # Check row
#             #         if row[other_tree_index] >= tree and other_tree_index < x_index:
#             #             w_visible = False
#             #         elif row[other_tree_index] >= tree and other_tree_index > x_index:
#             #             e_visible = False
#             #         # Check column
#             #         if data[other_tree_index][x_index] >= tree and other_tree_index > y_index:
#             #             n_visible = False
#             #         elif data[other_tree_index][x_index] >= tree and other_tree_index < y_index:
#             #             s_visible = False
#             #
#             #     # Only 1 direction needs to be visible
#             #     if w_visible or e_visible or n_visible or s_visible:
#             #         visible_count += 1
#     # return visible_count
#
#             # Part 2
#             current_score = 1
#             w_score = 0
#             e_score = 0
#             n_score = 0
#             s_score = 0
#             # Check west
#             for other_tree_index in range(x_index, -1, -1):
#                 if row[other_tree_index] < tree and other_tree_index != x_index:
#                     w_score += 1
#                     if other_tree_index == 0:
#                         current_score *= w_score
#                 elif row[other_tree_index] >= tree and other_tree_index != x_index:
#                     w_score += 1
#                     current_score *= w_score
#                     #print(w_score)
#                     break
#             # Check east
#             for other_tree_index in range(x_index, len(data)):
#                 if row[other_tree_index] < tree and other_tree_index != x_index:
#                     e_score += 1
#                     if other_tree_index == length:
#                         current_score *= e_score
#                 elif row[other_tree_index] >= tree and other_tree_index != x_index:
#                     e_score += 1
#                     current_score *= e_score
#                     break
#             # Check north
#             for other_tree_index in range(y_index, -1, -1):
#                 if data[other_tree_index][x_index] < tree and other_tree_index != y_index:
#                     n_score += 1
#                     if other_tree_index == 0:
#                         current_score *= n_score
#                 elif data[other_tree_index][x_index] >= tree and other_tree_index != y_index:
#                     n_score += 1
#                     current_score *= n_score
#                     break
#             # Check south
#             for other_tree_index in range(y_index, len(data)):
#                 if data[other_tree_index][x_index] < tree and other_tree_index != y_index:
#                     s_score += 1
#                     if other_tree_index == length:
#                         current_score *= s_score
#                 elif data[other_tree_index][x_index] >= tree and other_tree_index != y_index:
#                     s_score += 1
#                     current_score *= s_score
#                     break
#             #print(w_score,e_score, n_score,s_score, current_score)
#             scenic_scores.append(current_score)
#     #print(scenic_scores)
#     return max(scenic_scores)
#     ## This needs optimization or shortening
#

# Redone
with open('day8.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [[int(i) for i in k] for k in read_data]
    print(processed_data)


class TreeTop:
    def __init__(self, grid):
        self.grid = grid
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def main(self):
        print(self.count_visible())

    def find_neighbours(self, center):
        neighbours = []
        direction = []
        for d in self.directions:
            x, y = center
            for i in range(len(self.grid)):
                x, y = x + d[0], y + d[1]
                if 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid):
                    direction.append(self.grid[y][x])
                else:
                    break
            if direction:
                neighbours.append(direction)
                direction = []
        return neighbours

    def count_visible(self):
        count = 0
        scores = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                height = self.grid[y][x]
                neighbours = self.find_neighbours((x, y))
                if len(neighbours) < 4:
                    count += 1
                else:
                    for direction in neighbours:
                        if all(height > n for n in direction):
                            count += 1
                            break
                    # Part 2
                    scores.append(self.scenic_score(height, neighbours))
        return count, max(scores)

    def scenic_score(self, height, neighbours):
        s = 1
        for direction in neighbours:
            for i in range(len(direction)):
                if direction[i] >= height or i == len(direction) - 1:
                    s *= i + 1
                    break
        return s


if __name__ == '__main__':
    t = TreeTop(processed_data)
    t.main()
