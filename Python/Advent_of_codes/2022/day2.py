with open('day2.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [_.split() for _ in read_data]

elf_moves = {
    'A': 1,
    'B': 2,
    'C': 3
}


def eval_matches(matches):
    scores = 0
    for m in matches:
        if m[0] == m[1]:
            scores += m[1] + 3
        elif m[0] % 3 == m[1] - 1:
            scores += m[1] + 6
        else:
            scores += m[1]
    return scores


# Part 1
your_moves = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
matches = [[elf_moves[i[0]], your_moves[i[1]]] for i in processed_data]
print(eval_matches(matches))

# Part 2
your_moves = {
    'X': -1,
    'Y': 0,
    'Z': 1
}
matches = [[elf_moves[i[0]], (elf_moves[i[0]] - 1 + your_moves[i[1]]) % 3 + 1] for i in processed_data]
print(eval_matches(matches))
