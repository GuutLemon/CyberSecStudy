def flip_bin(inp):
    table = str.maketrans('01', '10')
    flipped = inp.translate(table)
    return flipped[::-1]

def fill_disk(inp, disk_len):
    while len(inp) < disk_len:
        flipped = flip_bin(inp)
        inp = inp + '0' + flipped
    return inp

def get_checksum(inp, disk_len):
    checksum = fill_disk(inp, disk_len)[:disk_len]
    while len(checksum) % 2 == 0:
        new_check = ''
        for i in range(0, len(checksum) - 1, 2):
            if checksum[i] == checksum[i+1]:
                new_check += '1'
            else:
                new_check += '0'
        checksum = new_check
    return checksum


if __name__ == '__main__':
    inp = '01111001100111011'
    disk_len1 = 272
    disk_len2 = 35651584

    print('Part 1: ', get_checksum(inp, disk_len1))
    print('Part 2: ', get_checksum(inp, disk_len2))
