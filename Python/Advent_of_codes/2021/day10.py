with open('day10.txt') as f:
    read_data = f.read().strip().split('\n')
    print(read_data)
    # Make a dict of parentheses
    parentheses = {
        '(': ')', '[': ']', '{': '}', '<': '>'
    }
    # Part 1
    scores = {
        ')': 3, ']': 57, '}': 1197, '>': 25137
    }
    first_syntax_error = []

    # Part 2
    incomplete = []
    ##

    for l in read_data:
        # Tracking open parentheses
        open_pos = []
        for i in range(len(l)):
            error = False
            p = l[i]
            if p in parentheses:
                open_pos.append(p)

            if len(open_pos) > 0:
                # Closing match
                if p == parentheses[open_pos[-1]]:
                    del open_pos[-1]
                # Closing not match
                elif p != parentheses[open_pos[-1]] and p in parentheses.values():
                    first_syntax_error.append(p)
                    error = True
                    break
            # Closing when empty
            elif len(open_pos) == 0 and p in parentheses.values():
                first_syntax_error.append(p)
                error = True
                break

        # Part 2
        if not error:
            incomplete.append(open_pos)
        ##

    print(first_syntax_error)
    total_scores = [scores[i] for i in first_syntax_error]
    print(sum(total_scores))

    # Part 2
    result = []
    for l in incomplete:
        complete = []
        for p in l[::-1]:
            closing_p = parentheses[p]
            complete.append(closing_p)
        result.append(complete)

    # Weird scoring system
    scores = {
        ')': 1, ']': 2, '}': 3, '>': 4
    }
    total_scores = []
    for l in result:
        current_score = 0
        for p in l:
            current_score = current_score *5 + scores[p]
        total_scores.append(current_score)
    print(total_scores)
    print(sorted(total_scores)[len(total_scores)//2])
