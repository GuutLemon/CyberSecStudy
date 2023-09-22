with open('day2.txt') as f:
    read_data = f.read().strip().split('\n')
    cmds = [[int(i) if i.isdigit() else i for i in j.split()] for j in read_data]

    def cal_pos(cmds):
        forwd = 0
        depth = 0
        aim = 0
        for c in cmds:
            cmd = c[0]
            dist = c[1]
            if cmd == 'forward':
                forwd += dist
                depth += aim * dist
            elif cmd == 'up':
                aim -= dist
            else:
                aim += dist
        return forwd * depth

    print(cal_pos(cmds))