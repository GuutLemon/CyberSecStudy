import re
import hashlib
from collections import defaultdict


def hashing(inp, hashed):
    md5_hash = hashlib.md5()
    md5_hash.update(inp.encode('utf-8'))
    hashed[inp] = md5_hash.hexdigest()

def hashing2(inp, hashed):
    new_salt = inp
    for i in range(2017):
        md5_hash = hashlib.md5()
        md5_hash.update(new_salt.encode('utf-8'))
        new_salt = md5_hash.hexdigest()
    hashed[inp] = new_salt


def check_hash1(inp, hashed, pattern):
    salt = inp[0] + str(inp[1])
    if salt not in hashed:
        hashing2(salt, hashed)      ######
    if searched := pattern.search(hashed[salt]):
        return salt, searched.group()

def check_hash2(inp, hashed, char):
    for i in range(1, 1000):
        salt = inp[0] + str(inp[1] + i)
        if salt not in hashed:
            hashing2(salt, hashed)      ######
        if char in hashed[salt]:
            # print(hashed[salt], salt, i)
            return salt


def find_password(inp, hashed):
    i = 0
    pattern = re.compile(r'(\w)\1\1')
    count = 0
    while count < 64:
        salt = [inp, i]
        if searched := check_hash1(salt, hashed, pattern):
            re_char = searched[1][0]*5
            if check_hash2(salt, hashed, re_char):
                count += 1
                print('Counting: ', count)
                # print(hashed[searched[0]], searched)
        i += 1
    return i - 1


if __name__ == '__main__':
    inp = 'ahsbgdzn'
    hashed = defaultdict()
    print('Part 2: ', find_password(inp, hashed))
