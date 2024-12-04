def is_word(inp, word, first_char_indx):
    count = 0
    l = len(word)
    directions = {(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)}
    for d in directions:
        to_check = word[0]
        i, j = first_char_indx[0], first_char_indx[1]
        for _ in range(l - 1):
            try:
                i += d[0]
                j += d[1]
                if i < 0 or j < 0:
                    break
                to_check += inp[i][j]
            except IndexError:
                break
        if to_check == word:
            count += 1
    return count

def is_word2(inp, word, mid_char_indx):
    word = set(word)
    directions = {((1, 1), (-1, -1)), ((-1, 1), (1, -1))}
    x, y = mid_char_indx[0], mid_char_indx[1]
    to_check = []
    for pair in directions:
        chars = set('A')
        for d in pair:
            try:
                i = x + d[0]
                j = y + d[1]
                if i < 0 or j < 0:
                    break
                chars.add(inp[i][j])
            except IndexError:
                break
        to_check.append(chars)
    if all(chars == word for chars in to_check):
        return 1
    return 0


def count_word(inp, word1='XMAS', word2='MAS'):
    count1 = 0
    count2 = 0
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == word1[0]:
                count1 += is_word(inp, word1, (i, j))
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == word2[1]:
                count2 += is_word2(inp, word2, (i, j))
    return count1, count2


if __name__ == '__main__':
    with open('day04.txt') as f:
        INP = f.read().strip().split('\n')

    solve = count_word(INP)
    print('Part 1: ', solve[0])
    print('Part 2: ', solve[1])