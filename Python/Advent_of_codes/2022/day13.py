with open('day13.txt') as f:
    read_data = f.read().strip().split('\n\n')
    processed_data = [[eval(i) for i in j.split('\n')] for j in read_data]
    print(processed_data)


class Signals:
    def __init__(self, sigs):
        self.sigs = sigs[::]

    def main(self):
        count = []
        for s in range(len(self.sigs)):
            if self.comparing(self.sigs[s][0], self.sigs[s][1]) > 0:
                count.append(s + 1)
                # print(s+1, 'good')
        print(sum(count))
        self.sorting()
        result2 = 1
        for i in range(len(self.sigs)):
            if self.sigs[i] == [[2]] or self.sigs[i] == [[6]]:
                result2 *= i + 1
        print(result2)

    def comparing(self, inp1, inp2):
        if type(inp1) == type(inp2) == int:
            if inp1 < inp2:
                return 1
            if inp1 == inp2:
                return 0
            return -1
        if type(inp1) != type(inp2):
            if type(inp1) == int:
                inp1 = [inp1]
            if type(inp2) == int:
                inp2 = [inp2]
            return self.comparing(inp1, inp2)

        for a, b in zip(inp1, inp2):
            result = self.comparing(a, b)
            if result:
                return result
        return len(inp2) - len(inp1)

    def sorting(self):
        self.sigs = [i for j in self.sigs for i in j]
        self.sigs.extend([[[2]], [[6]]])
        for i in range(len(self.sigs)):
            for j in range(len(self.sigs) - i - 1):
                if self.comparing(self.sigs[j], self.sigs[j + 1]) <= 0:
                    self.sigs[j], self.sigs[j + 1] = self.sigs[j + 1], self.sigs[j]


if __name__ == '__main__':
    s = Signals(processed_data)
    s.main()
