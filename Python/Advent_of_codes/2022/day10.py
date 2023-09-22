
#
#     x = 1
#     signals = []
#     adding = 0
#     ##### Part 2
#     current_sprite = (0, 1, 2)
#     screen = []
#     line = []
#     ############
#     for i in range(len(processed_data)):
#         if processed_data[i][0] == 'addx':
#             adding = processed_data[i][1]
#         elif adding != 0:
#             x += adding
#             adding = 0
#
#         # Part 2
#             current_sprite = (x - 1, x, x + 1)
#         #print(current_sprite, i % 40)
#         if i % 40 in current_sprite:
#             line.append('#')
#         else:
#             line.append('.')
#         if i in (39, 79, 119, 159, 199, 239):
#             screen.append(line)
#             line = []
#
#         # Part 1
#         if i + 1 in (20, 60, 100, 140, 180, 220):
#             signals.append(x * (i + 1))
#         #print(i, processed_data[i], x, adding)
#
#
#     print(sum(signals))
#     for line in screen:
#         print(''.join(line))

# Redone
with open('day10.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = []
    # Add empty cycles
    for i in read_data:
        if i.startswith('add'):
            i = i.split()
            processed_data.append(['empty'])
            processed_data.append([i[0], int(i[1])])
        else:
            processed_data.append(i.split())
    print(processed_data)


class CathodeTube:
    def __init__(self, code):
        self.code = code
        self.x = 1
        self.signals = []
        self.screen = []
        self.line = []

    def main(self):
        self.cal_x()
        print(sum(self.signals))
        self.print_screen()

    def cal_x(self):
        add = 0
        for i in range(len(self.code)):
            # Load value for next cycle
            if self.code[i][0] == 'addx':
                add = self.code[i][1]
            # Add previous cycle's value to x
            elif add != 0:
                self.x += add
                # Reset value
                add = 0
            self.get_signal(i)
            self.draw_screen(i, self.x)

    def get_signal(self, i):
        turn = i + 1
        if turn in (-20 + 40 * (_ + 1) for _ in range(6)):
            self.signals.append(self.x * turn)

    def draw_screen(self, i, x):
        turn = i + 1
        checking = (x - 1, x, x + 1)
        if i % 40 in checking:
            sprite = '#'
        else:
            sprite = '.'
        self.line.append(sprite)
        if turn in (40 * (_ + 1) for _ in range(6)):
            self.screen.append(self.line)
            self.line = []

    def print_screen(self):
        for line in self.screen:
            print(' '.join(line))


if __name__ == '__main__':
    c = CathodeTube(processed_data)
    c.main()