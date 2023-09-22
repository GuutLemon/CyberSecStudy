with open('day20.txt') as f:
    read_data = f.read().strip().split('\n')
    nums = [int(_) for _ in read_data]


class Mixing:
    def __init__(self, nums):
        self.original = {j: i for i, j in enumerate(nums)}  # Tag each number
        self.nums = [(j, i) for i, j in enumerate(nums)]    # to keep track of them when moving

    def main(self):
        self.mixing()
        grove_coord = [_[0] for _ in list(self.find_coord())[1:]]
        print(sum(grove_coord))

    def mixing(self):
        for num, tag in self.original.items():
            current_pos = self.nums.index((num, tag))
            l = len(self.original)
            new_pos = (current_pos + num) % l
            self.nums = self.nums[:current_pos] + self.nums[current_pos+1:new_pos] + [(num, tag)] + self.nums[new_pos:]
            print(current_pos, num, new_pos)
            print(self.nums)

    def find_coord(self):
        tag = self.original[0]
        pos = self.nums.index((0, tag))
        for i in range(3001):
            if i % 1000 == 0:
                yield self.nums[pos]
            pos = (pos + 1) % len(self.nums)


if __name__ == '__main__':
    m = Mixing(nums)
    m.main()

