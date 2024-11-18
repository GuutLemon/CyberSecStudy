def count_valid(lst, part):
    count = 0
    if part == 1:
        for p in lst:
            if any(p.count(word) > 1 for word in p):
                continue
            count += 1
        return count
    else:
        for p in lst:
            if any(p.count(word) > 1 for word in p):
                continue
            word_counts = dict()
            for word in p:
                word_counts.update({word: {char: word.count(char) for char in word}})
            if any(list(word_counts.values()).count(v) > 1 for v in word_counts.values()):
                continue
            count += 1
        return count


if __name__ == '__main__':
    with open('day04.txt') as f:
        passphrases = f.read().strip().split('\n')
        passphrases = [_.split() for _ in passphrases]

    print('Part 1: ', count_valid(passphrases, 1))
    print('Part 2: ', count_valid(passphrases, 2))

