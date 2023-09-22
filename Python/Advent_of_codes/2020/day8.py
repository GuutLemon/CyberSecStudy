with open('day8.txt') as f:
    read_data = f.read().strip().split('\n')
    cmds = [[eval(i) if i[-1].isdigit() else i for i in k.split()] for k in read_data]
    cmds = [cmds[i] + [i] for i in range(len(cmds))]    # Add turn
    print(cmds)


def cal_acc(cmds, cmds_lst=[], count=0, turn=0):
    for c in cmds[turn:]:
        if c[2] in cmds_lst:
            # print(cmds_lst, c[2], count)
            return 'loop', count
        cmds_lst.append(c[2])
        if c[0] == 'acc':
            count += c[1]
        elif c[0] == 'jmp':
            turn = c[2] + c[1]
            return cal_acc(cmds, cmds_lst, count, turn)
    return 'ter', count

# Part 1
print(cal_acc(cmds)[1])

# Part 2
for i, c in enumerate(cmds):
    if c[0] == 'nop':
        cmds[i][0] = 'jmp'
        result = cal_acc(cmds, cmds_lst=[], count=0, turn=0)
        if result[0] == 'ter':
            print(result[1])
            break
        cmds[i][0] = 'nop'
    elif c[0] == 'jmp':
        cmds[i][0] = 'nop'
        result = cal_acc(cmds, cmds_lst=[], count=0, turn=0)
        if result[0] == 'ter':
            print(result[1])
            break
        cmds[i][0] = 'jmp'
