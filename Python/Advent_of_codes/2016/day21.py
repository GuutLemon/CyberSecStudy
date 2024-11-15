from collections import deque


class Scrambling:
    def __init__(self, string, instructions):
        self.string = deque(string)
        self.instructions = instructions

    def get_str(self):
        return ''.join(self.string)

    def swap(self, pair):
        if isinstance(pair[0], str):
            x = pair[0]
            x_indx = self.string.index(x)
        else:
            x_indx = pair[0]
            x = self.string[x_indx]
        if isinstance(pair[1], str):
            y = pair[1]
            y_indx = self.string.index(y)
        else:
            y_indx = pair[1]
            y = self.string[y_indx]
        self.string[x_indx] = y
        self.string[y_indx] = x

    def rotate(self, inp):
        if len(inp) == 2:
            dir = inp[0]
            steps = inp[1]
            if dir == 'right':
                self.string.rotate(steps)
            else:
                self.string.rotate(-steps)
        else:
            char_indx = self.string.index(inp[0])
            if char_indx >= 4:
                self.string.rotate(1 + char_indx + 1)
            else:
                self.string.rotate(1 + char_indx)

    def reverse(self, pos):
        x = pos[0]
        y = pos[1]
        s = self.get_str()
        s = s[:x] + s[x:y+1][::-1] + s[y+1:]
        self.string = deque(s)

    def move(self, pos):
        x_indx = pos[0]
        x = self.string[x_indx]
        y_indx = pos[1]
        del self.string[x_indx]
        self.string.insert(y_indx, x)

    def run_insrt(self):
        for instr in self.instructions:
            if instr[0] == 'swap':
                self.swap(instr[1:])
            elif instr[0] == 'rotate':
                self.rotate(instr[1:])
            elif instr[0] == 'reverse':
                self.reverse(instr[1:])
            elif instr[0] == 'move':
                self.move(instr[1:])

    def reverse_instr(self):
        for instr in self.instructions[::-1]:
            if instr[0] == 'swap':
                self.swap(instr[1:])
            elif instr[0] == 'reverse':
                self.reverse(instr[1:])
            elif instr[0] == 'move':
                self.move(instr[1:][::-1])
            elif instr[0] == 'rotate':
                if len(instr) == 3:
                    self.rotate([instr[1], -instr[2]])
                else:
                    self.rotate2(instr[1])

    def rotate2(self, char):
        char_indx = self.string.index(char)
        if char_indx in {1, 3, 5, 7}:
            self.string.rotate(-(char_indx // 2) - 1)
        else:
            char_indx = ((char_indx - 2) % len(self.string) + len(self.string)) // 2
            self.string.rotate(-char_indx - 2)


if __name__ == '__main__':
    with open('day21.txt') as f:
        instructions = f.read().strip()
        words = ['letter ', 'with ', 'position ', 'positions ', 'to ', 'through ', 'steps', 'step', 'based on ', 'of ']
        for w in words:
            instructions = instructions.replace(w, '')
        instructions = [[int(i) if i.isdigit() else i for i in j.split()] for j in instructions.split('\n')]

    s = Scrambling('abcdefgh', instructions)
    s.run_insrt()
    print('Part 1: ',s.get_str())

    s = Scrambling('fbgdceah', instructions)
    s.reverse_instr()
    print('Part 2: ', s.get_str())
