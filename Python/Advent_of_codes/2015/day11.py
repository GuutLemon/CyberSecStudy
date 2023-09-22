def increase_word(word, increment):
    result = ''
    char = word[-1]
    value = ord(char.lower()) - ord('a')

    if (value + increment) <= 25:
        result = chr(value + increment + ord('a'))
        #print(value + increment)
        return word[:-1] + result
    else:
        leftover = (value + increment) % 26
        carry = (value + increment) // 26
        #print(leftover)
        #print(carry)
        result = chr(leftover + ord('a'))
        if len(word) == 1:
            if carry <= 25:
                return chr(carry + ord('a') - 1) + result
            else:
                return increase_word(word, carry) + result
        return increase_word(word[:-1], carry) + result


def check_pass(passwd):
    alphabets = list(map(chr, range(ord('a'), ord('z') + 1)))
    xyz = [alphabets[i:i + 3] for i in range(len(alphabets) - 2)]
    #print(xyz)
    excluded = ['i', 'o', 'l']
    check_xyz = False
    check_pairs = False
    rep_check = ''
    count_pairs = 0

    for l in excluded:
        if l in passwd:
            return

    for w in xyz:
        if "".join(w) in passwd:
            #print(w)
            #print("".join(w))
            check_xyz = True
            break

    for i in range(len(passwd)):
        if i < len(passwd) - 1:
            if passwd[i] == passwd[i+1] and passwd[i] != rep_check:
                count_pairs += 1
                rep_check = passwd[i]
            else:
                continue
        if count_pairs == 2:
            check_pairs = True
            break

    if check_pairs and check_xyz:
        return passwd


word = "vzbxxzaa"
while True:
    if check_pass(word):
        print(word)
        break
    word = increase_word(word, 1)
    #print(word)

#print(increase_word('a', 26))