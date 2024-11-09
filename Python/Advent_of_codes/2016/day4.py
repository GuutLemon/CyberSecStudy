import re

with open('day4.txt') as f:
    encrypted = f.read().strip().split('\n')
    encrypted = [re.split(r'(\d+)', _) for _ in encrypted]


def check_id(rooms):
    id_sum = 0
    real_rooms = []
    for r in rooms:
        id = int(r[1])
        checksum = r[2][1:-1]
        name = r[0].replace('-', '')
        word_count = {}
        for letter in name:
            if letter not in word_count:
                word_count[letter] = name.count(letter)
        sorted_count = sorted(word_count.items(), key=lambda count: (-count[1], count[0]))
        token = ''.join([i[0] for i in sorted_count[:len(checksum)]])
        if token == checksum:
            id_sum += id
            real_rooms.append(r)

    # Part 2
    decrypted = []
    for r in real_rooms:
        id = int(r[1])
        name = r[0]
        rot_name = ''
        for letter in name:
            if letter != '-':
                rot = (ord(letter) - 97 + id) % 26
                new_char = chr(rot + 97)
                rot_name += new_char
            else:
                rot_name += ' '
        decrypted.append((rot_name, id))
    for r in decrypted:
        if 'object' in r[0]:
            secret_id = r[1]

    return id_sum, secret_id



if __name__ == '__main__':
    solve = check_id(encrypted)
    print('Part 1: ', solve[0])
    print('Part 2: ', solve[1])


