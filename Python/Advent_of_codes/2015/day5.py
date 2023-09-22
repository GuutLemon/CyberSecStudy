import re


# Part 1
# Practicing conditional because regex would be too easy
def nice_string_check1(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_check = []
    dup = False
    vow = False
    # Check bad strings
    bad_str = ['ab', 'cd', 'pq', 'xy']
    for bad in bad_str:
        if bad in ''.join(string):
            return None
    # Check vowels
    for letter in string:
        if letter in vowels:
            vowels_check.append(letter)
    if len(vowels_check) >= 3:
        vow = True
    # Check duplicate letters
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            dup = True
            break
    if dup and vow:
        return string


# Part 2
def nice_string_check2(string):
    repeat_pair = False
    xyx = False
    for i, l in enumerate(string):
        # Prevent IndexError
        if i < len(string) - 1:
            pattern1 = f".*{l}{string[i+1]}.*{l}{string[i+1]}.*"
            pattern2 = f".*{l}\w{l}.*"
            if re.search(pattern1, string):
                repeat_pair = True
            if re.search(pattern2, string):
                xyx = True
        if repeat_pair and xyx:
            return string


with open('day5.txt') as f:
    read_data = f.read().strip().split('\n')
    count1 = 0
    count2 = 0
    for i in read_data:
        if nice_string_check1(i):
            count1 += 1
        if nice_string_check2(i):
            count2 += 1
    print(count1)
    print(count2)