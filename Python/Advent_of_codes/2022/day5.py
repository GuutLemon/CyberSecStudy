with open('day5.txt') as f:
    read_data = f.read().strip().split('\n\n')
    stacks_data = read_data[0].split('\n')
    cmds = [[int(j.split()[i]) for i in range(1, len(j.split()), 2)] for j in read_data[1].split('\n')]
    print(cmds)

    stacks = {}
    for i in stacks_data[::-1][1:]:
        col = 0
        for j in range(1, len(i), 4):
            col += 1
            if col not in stacks:
                stacks[col] = []
            if i[j].isalpha():
                stacks[col].append(i[j])
    print(stacks)


class Crane:
    def __init__(self, cmds, stacks):
        self.cmds = cmds
        self.stacks = stacks

    def main(self):
        # self.moving1()
        self.moving2()
        print(''.join([i[-1] for i in list(self.stacks.values())]))

    def moving1(self):
        for c in self.cmds:
            amount = c[0]
            start = c[1]
            end = c[2]
            for a in range(amount):
                self.stacks[end].append(self.stacks[start].pop())

    def moving2(self):
        for c in self.cmds:
            amount = c[0]
            start = c[1]
            end = c[2]
            self.stacks[end].extend(self.stacks[start][-amount:])
            del stacks[start][-amount:]


c = Crane(cmds, stacks)
c.main()

