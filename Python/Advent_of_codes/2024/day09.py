from collections import deque


def get_blocks(disk_map):
    blocks = []
    block_name = 0
    for i, n in enumerate(disk_map):
        size = int(n)
        if i % 2 == 0:
            blocks.append([block_name, size])
            block_name += 1
        else:
            if size > 0:
                blocks.append(['.', size])
    return blocks

def sort_disk(blocks):
    i = 1
    while True:
        try:
            blocks[i + 1]
        except IndexError:
            return
        print(blocks)
        first_empties = blocks[i][1]
        last_non_empties = blocks[-1][1]
        if first_empties >= last_non_empties:
            blocks[i][1] = first_empties - last_non_empties
            blocks.insert(i, blocks[-1])
            blocks.pop()
            if '.' in blocks[-1]:
                blocks.pop()
            i += 1
        else:
            blocks[i][0] = blocks[-1][0]
            blocks[-1][1] = last_non_empties - first_empties
            i += 2

def sort_disk2(blocks):
    j = -1
    max_id = blocks[-1][0]
    while abs(j) <= len(blocks) - 1:
        if '.' not in blocks[j] and blocks[j][0] <= max_id:
            max_id = blocks[j][0]
            i = next(blocks.index(_) for _ in blocks if '.' in _)
            while i < len(blocks) - 1 - abs(j):
                current_empties = blocks[i][1]
                current_non_empties = blocks[j][1]
                if '.' in blocks[i] and  current_empties >= current_non_empties:
                    # print(blocks[i], blocks[j])
                    # print(blocks)
                    blocks[i][1] = current_empties - current_non_empties
                    if blocks[i][1] == 0:
                        blocks[i] = [blocks[j][0], blocks[j][1]]
                    else:
                        blocks.insert(i, blocks[j].copy())
                        i += 1
                    blocks[j][0] = '.'
                    if '.' in blocks[j - 1]:
                        blocks[j][1] += blocks[j - 1][1]
                        del blocks[j - 1]
                    if '.' in blocks[j + 1]:
                        blocks[j][1] += blocks[j + 1][1]
                        del blocks[j + 1]
                    i += 1
                    break
                i += 1
        j -= 1


def get_checksum(disk_map, part=1):
    blocks = deque(get_blocks(disk_map))
    sorted_disk = []
    checksum = 0
    if part == 2:
        sort_disk2(blocks)
    else:
        sort_disk(blocks)
    for b in blocks:
        for i in range(b[1]):
            sorted_disk.append(b[0])
    print(sorted_disk)
    for i, n in enumerate(sorted_disk):
        if n != '.':
            checksum += i * int(n)
    return checksum


if __name__ == '__main__':
    with open('day09.txt') as f:
        INP = f.read().strip()

    # INP = '2333133121414131402'

    print(get_checksum(INP, 2))
