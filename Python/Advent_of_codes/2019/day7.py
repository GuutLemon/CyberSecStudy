from day5 import intcode
from itertools import permutations

with open('day7.txt') as f:
    read_data = f.read().strip()
    processed_data = eval('[' + read_data + ']')


class Amplifier():
    def __init__(self, code):
        self.phases1 = list(permutations([0, 1, 2, 3, 4]))       # Part 1
        self.phases2 = list(permutations([5, 6, 7, 8, 9]))
        self.code = code
        self.max = []

    def main(self):
        # print(self.cal_max_output1())
        print(self.cal_max_output2())

    def cal_max_output1(self):
        for phases in self.phases1:
            output = 0
            for p in phases:
                inp = [p, output]
                code = self.code
                output = list(intcode(code, inp))[0]
            self.max.append(output)
        return max(self.max)

    def cal_max_output2(self):
        for phases in self.phases2:
            output = 0
            for p in phases:
                inp = [p, output]
                code = self.code
                output = list(intcode(code, inp))
                print(output)


a = Amplifier(processed_data)
a.main()