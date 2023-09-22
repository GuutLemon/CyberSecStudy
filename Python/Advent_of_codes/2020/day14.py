import re
from itertools import product


with open('day14.txt') as f:
    read_data = f.read().strip().split('\n')


class Masking():
    def __init__(self, inp):
        self.inp = inp
        self.mask = ''
        self.mem = {}

    def main(self):
        for l in self.inp:
            if l.startswith('mem'):
                # exec('self.'+l)
                # self.get_mem_value1(l)
                self.get_mem_value2(l)
            else:
                self.mask = [int(_) if _.isdigit() else _ for _ in l.split()[-1]]
        return sum(list(self.mem.values()))

    def get_mem_value1(self, line):
        mem_result = []
        current_mem_locat = int(re.search(r'\[(\d+)\]', line).group(1))
        mem_bin = list(bin(self.mem[current_mem_locat])[2:])
        # print(mem_bin, self.mask)
        for i in range(-1, -len(self.mask) - 1, -1):
            if i >= -len(mem_bin):
                a = mem_bin[i]
            else:
                a = '0'
            if self.mask[i] == 1:
                mem_result.insert(0, str(self.mask[i] | int(a)))
            elif self.mask[i] == 0:
                mem_result.insert(0, str(self.mask[i] & int(a)))
            else:
                mem_result.insert(0, a)
            # print(''.join(mem_result), self.mask[i], a)
        # print(''.join(mem_result))
        mem_result = int(''.join(mem_result), 2)
        self.mem[current_mem_locat] = mem_result

    # Part 2
    def get_mem_value2(self, line):
        mem_result = []
        current_mem_locat = int(re.search(r'\[(\d+)\]', line).group(1))
        value = int(line.split()[-1])
        locat_bin = list(bin(current_mem_locat)[2:])
        len_mask = self.get_len(self.mask)
        len_locat = self.get_len(locat_bin)
        max_len = max(len_mask, len_locat)

        # print(mem_bin, self.mask)
        for i in range(-1, -max_len - 1, -1):
            if self.mask[i] == 0:
                if i >= -len_locat:
                    mem_result.insert(0, locat_bin[i])
                else:
                    mem_result.insert(0, str(self.mask[i]))
            elif self.mask[i] == 1:
                mem_result.insert(0, '1')
            else:
                mem_result.insert(0, 'X')
            # print(''.join(mem_result), self.mask[i], a)
        # print(''.join(mem_result))
        self.assign_mem(mem_result, value)

    def get_len(self, bin):
        bin_len = 0
        for i in range(len(bin)):
            if bin[i] != 0:
                bin_len = len(bin) - i
                return bin_len

    def assign_mem(self, mem, value):
        indx = []
        result = []
        for i in range(len(mem)):
            if mem[i] == 'X':
                indx.append(i)

        combs = list(product(['0', '1'], repeat=len(indx)))
        for c in combs:
            for i in range(len(indx)):
                mem[indx[i]] = c[i]
            result.append(''.join(mem))
        # print(result)

        for r in result:
            location = int(r, 2)
            self.mem[location] = value
        # print(self.mem)


a = Masking(read_data)
print(a.main())