with open('day7.txt') as f:
    read_data = f.read().strip().split('\n')


class BuildFileSystem:
    def __init__(self, data):
        self.data = data
        self.pwd = ['home']
        self.map = {'home': 0}

    def main(self):
        self.build()
        for d in self.map:
            self.cal_dir_size(d)
        result1 = 0
        for size in self.map.values():
            if size <= 100000:
                result1 += size
        print(f'Part1: {result1}')
        print(f'Part2: {self.free_up_space()}')

    def build(self):
        for d in self.data:
            d = d.split()
            if d[1] == 'cd':
                if d[-1] == '/':
                    self.pwd = ['home']
                elif d[-1] == '..':
                    del self.pwd[-1]
                else:
                    self.pwd.append(d[-1])
            elif d[0] == 'dir':
                new_dir = '/'.join(self.pwd) + f'/{d[1]}'
                self.map[new_dir] = 0
            elif d[0].isdigit():
                current_dir = '/'.join(self.pwd)
                self.map[current_dir] += int(d[0])

    def cal_dir_size(self, dir):
        size = self.map[dir]
        for i in range(len(dir.split('/')) - 1):
            dir = dir[:dir.rfind('/')]
            self.map[dir] += size

    def free_up_space(self):
        total_size = 70000000
        update_size = 30000000
        unused = total_size - self.map['home']
        needed_size = update_size - unused
        valid_dir_size = []
        for size in self.map.values():
            if size >= needed_size:
                valid_dir_size.append(size)
        return min(valid_dir_size)


if __name__ == '__main__':
    b = BuildFileSystem(read_data)
    b.main()



