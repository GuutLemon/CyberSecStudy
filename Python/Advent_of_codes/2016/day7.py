import re


def sep_brackets(strings):
    result = []
    pattern = re.compile(r'(\[.*?])')
    for s in strings:
        s = pattern.split(s)
        result.append(s)
    return result

# Part 1
def find_seq(string):
    for i in range(len(string) - 3):
        if string[i] + string[i+1] == string[i+3] + string[i+2] and string[i] != string[i+1]:
            return True
    return False

def count_tls(lst):
    count = 0
    for ip in lst:
        seq_outside = 0
        seq_inside = 0
        for part in ip:
            seq = find_seq(part)
            if not part.startswith('[') and seq:
                seq_outside += 1
            elif part.startswith('[') and seq:
                seq_inside += 1
        if seq_outside > 0 and seq_inside == 0:
            count += 1
    return count

# Part 2
def find_ssl(string):
    ssl = []
    for i in range(len(string) - 2):
        if string[i] == string[i+2] != string[i+1]:
            ssl.append(string[i] + string[i+1] + string[i+2])
    return ssl

def count_ssl(lst):
    count = 0
    for ip in lst:
        seq_outside = []
        seq_inside = []
        for part in ip:
            seq = find_ssl(part)
            if not part.startswith('[') and seq:
                seq_outside.extend(seq)
            elif part.startswith('[') and seq:
                seq_inside.extend(seq)
        for s in seq_outside:
            s = s[1] + s[0] + s[1]
            if s in seq_inside:
                count += 1
                break
    return count

if __name__ == '__main__':
    with open('day7.txt') as f:
        IPs = f.read().strip().split('\n')
    IPs = sep_brackets(IPs)
    print('Part 1: ', count_tls(IPs))
    print('Part 2: ', count_ssl(IPs))


