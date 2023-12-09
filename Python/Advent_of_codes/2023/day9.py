with open('day9.txt') as f:
    read_data = f.read().strip().split('\n')

inp = [list(map(int, i.split())) for i in read_data]


class NumSequence:
    def __init__(self, inp):
        self.inp = inp
        self.step_map = self.map_seq()
        self.next_num = self.generate_next_num()
        self.prev_num = self.generate_previous_num()

    def __repr__(self):
        return f'{self.step_map}'

    def map_seq(self):
        mapped = [self.inp]
        current_seq = self.inp
        while any(i != 0 for i in current_seq):
            current_seq = list(map(lambda x: current_seq[x + 1] - current_seq[x], range(len(current_seq) - 1)))
            mapped.append(current_seq)
        return mapped

    def generate_next_num(self):
        next = 0
        for seq in self.step_map[::-1]:
            next += seq[-1]
        return next

    def generate_previous_num(self):
        prev = 0
        for seq in self.step_map[::-1]:
            prev = seq[0] - prev
        return prev


sequenced = [NumSequence(i) for i in inp]
print('Part 1:', sum(sq.next_num for sq in sequenced))
print('Part 2:', sum(sq.prev_num for sq in sequenced))
