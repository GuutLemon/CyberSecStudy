import re
import hashlib


def find_password1(inp):
    passwd = ''
    i = 0
    while len(passwd) < 8:
        test = inp + str(i)
        md5_hash = hashlib.md5()
        md5_hash.update(test.encode('utf-8'))
        hash = md5_hash.hexdigest()
        if re.search('^0{5}.*', hash):
            passwd += hash[5]
            print('Hashing: ', passwd)
        i += 1
    return passwd

def find_password2(inp):
    passwd = [None]*8
    i = 0
    while not all(i for i in passwd):
        test = inp + str(i)
        md5_hash = hashlib.md5()
        md5_hash.update(test.encode('utf-8'))
        hash = md5_hash.hexdigest()
        if re.search('^0{5}.*', hash):
            if hash[5].isdigit() and int(hash[5]) < 8 and not passwd[int(hash[5])] :
                passwd[int(hash[5])] = hash[6]
                print('Hashing: ', passwd)
        i += 1
    return ''.join(passwd)


if __name__ == '__main__':
    inp = 'reyedfim'
    print('Part 1: ', find_password1(inp))
    print('Part 2: ', find_password2(inp))
