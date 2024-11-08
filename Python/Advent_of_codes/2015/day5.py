with open('day5.txt') as f:
    strings = f.read().strip().split('\n')

# Part 1
def str_check1(s):
    vowels = 'aeiou'
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    double_letter = False
    vowels_check = False
    vowels_count = 0

    for b in bad_strings:
        if b in s:
            return False

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            double_letter = True
            break
    if not double_letter:
        return False

    for i in s:
        if i in vowels:
            vowels_count += 1
        if vowels_count >= 3:
            vowels_check = True
            break
    if not vowels_check:
        return False
    return True

# Part 2
def str_check2(s):
    pair = False
    xyx = False
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            xyx = True
            break
    if not xyx:
        return False

    for i in range(len(s) - 2):
        if s[i]+s[i+1] in s[i+2:]:
            pair = True
            break
    if not pair:
        return False
    return True


count1 = 0
count2 = 0
for s in strings:
    if str_check1(s):
        count1 += 1
    if str_check2(s):
        count2 += 1
print(count1, '\n', count2)

