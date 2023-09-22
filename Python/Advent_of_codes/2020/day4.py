import re

with open('day4.txt') as f:
    read_data = f.read().strip().replace('\n', ' ').replace(':', ' ').split('  ')
    passports = [{j.split()[i]: j.split()[i + 1] for i in range(0, len(j.split()) - 1, 2)} for j in read_data]
    fields = ['byr', 'ecl', 'pid', 'eyr', 'hcl', 'iyr', 'cid', 'hgt']

    # Part 1
    valid1 = []
    for p in passports:
        if len(p) == len(fields) or (len(p) == len(fields) - 1 and 'cid' not in p):
            valid1.append(p)
    print(len(valid1))

    # Part 2
    valid2 = []
    for p in valid1:
        if int(p['byr']) in range(1920, 2003) and \
                int(p['iyr']) in range(2010, 2021) and \
                int(p['eyr']) in range(2020, 2031) and \
                ((p['hgt'].endswith('cm') and int(p['hgt'][:-2]) in range(150, 194)) or
                 (p['hgt'].endswith('in') and int(p['hgt'][:-2]) in range(59, 77))) and \
                re.search('^#[0-9a-f]{6}$', p['hcl']) and \
                p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
                re.search('^[0-9]{9}$', p['pid']):
            valid2.append(p)
    print(len(valid2))
