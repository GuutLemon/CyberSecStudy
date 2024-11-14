from collections import deque

def elf_steal1(lst):
    if len(lst) % 2 == 0:
        lst = lst[::2]
    else:
        lst = lst[::2]
        lst = lst[-1:] + lst[:-1]
    return lst

def lucky_elf1(n):
    elfs = [i for i in range(1, n + 1)]
    while len(elfs) > 1:
        elfs = elf_steal1(elfs)
    return elfs[0]

def lucky_elf2(n):
    elfs = [i for i in range(1, n + 1)]
    elfs = deque(elfs)
    while len(elfs) > 1:
        middle_indx = len(elfs) // 2
        del elfs[middle_indx]
        elfs.rotate(-1)
        # print(len(elfs))
        # print(elfs)
    return elfs[0]


if __name__ == '__main__':
    elfs_num = 3014387
    print('Part 1: ', lucky_elf1(elfs_num))
    print('Part 2 is gonna take 2 hours', '\n', 'Part 2: ', lucky_elf2(elfs_num))


