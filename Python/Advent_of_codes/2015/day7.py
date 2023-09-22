def eval_signal(board: dict, wire: str, signals: dict) -> int:
    instruct = board[wire]
    if wire.isdigit():
        return int(wire)
    elif wire in signals:
        return signals[wire]

    elif len(instruct) == 1:
        if instruct[0].isdigit():
            signals[wire] = int(instruct[0])
        else:
            signals[wire] = eval_signal(board, instruct[0], signals)

    elif len(instruct) == 2:
        if instruct[1].isdigit():
            signals[wire] = ~ int(instruct[1])
        signals[wire] = ~ eval_signal(board, instruct[1], signals) & 0xffff

    elif len(instruct) == 3:
        operator = instruct[1]
        if instruct[0].isdigit():
            part1 = int(instruct[0])
        else:
            part1 = eval_signal(board, instruct[0], signals)
        if instruct[2].isdigit():
            part2 = int(instruct[2])
        else:
            part2 = eval_signal(board, instruct[2], signals)
        if operator == "AND":
            signals[wire] = part1 & part2
        elif operator == "OR":
            signals[wire] = part1 | part2
        elif operator == "RSHIFT":
            signals[wire] = part1 >> part2
        elif operator == "LSHIFT":
            signals[wire] = part1 << part2
    return signals[wire]

with open("day7.txt") as f:
    board = {}
    signals = {}
    read_data = f.read().strip().split("\n")
    for _ in read_data:
        intruct, wire = _.strip().split(" -> ")
        board[wire] = intruct.split()
    # Part 1
    signals['a'] = eval_signal(board, 'a', signals)
    print(signals['a'])

    # Part 2
    b_val = signals['a']
    signals = {}
    board['b'] = [str(b_val)]
    signals['a'] = eval_signal(board, 'a', signals)
    print(signals['a'])