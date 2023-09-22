import re
import hashlib


def hash_check(inp):
    i = 0
    while True:
        result = inp + str(i)
        md5_hash = hashlib.md5()
        md5_hash.update(result.encode('utf-8'))
        # Part 1
        if re.search('^0{5}.*', md5_hash.hexdigest()):
            return result
        i += 1
        # Part 2: ^0{6}.*


inp = 'iwrupvqb'
print(hash_check(inp))

