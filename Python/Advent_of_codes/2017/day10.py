def knotting(inp, lst_size, part=1):
    lst = [_ for _ in range(lst_size)]
    i = 0
    skip_size = 0
    if part == 2:
        loop = 64
    else:
        loop = 1
    for l in range(loop):
        for twist_len in inp:
            lst = lst[i:] + lst[:i]
            lst = lst[:twist_len][::-1] + lst[twist_len:]
            lst = lst[len(lst)-i:] + lst[:len(lst)-i]
            i = (i + twist_len + skip_size) % lst_size
            skip_size += 1
    return lst

def cal_dense_hash(lst, lst_size):
    dense_hash = []
    for i in range(0, lst_size, 16):
        n = lst[i]
        for j in range(i + 1, i + 16):
            n ^= lst[j]
        dense_hash.append(n)
    return dense_hash

def cal_hex_hash(lst):
    result = []
    for i in range(len(lst)):
        x = format(lst[i], 'x')
        if len(x) == 1:
            x = '0' + x
        result.append(x)
    return ''.join(result)

def knot_hashing(inp, lst_size):
    sparse_hash = knotting(inp, lst_size, 2)
    dense_hash = cal_dense_hash(sparse_hash, lst_size)
    hex_hash = cal_hex_hash(dense_hash)
    return hex_hash


if __name__ == '__main__':
    SIZE = 256
    INP = '199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192'
    INP1 = [int(_) for _ in INP.split(',')]
    INP2 = [ord(_) for _ in INP]
    TAIL = [17, 31, 73, 47, 23]
    INP2.extend(TAIL)

    part1 = knotting(INP1, SIZE)
    print('Part 1: ', part1[0] * part1[1])
    print('Part 1: ', knot_hashing(INP2, SIZE))
