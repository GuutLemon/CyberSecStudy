with open('day4.txt') as f:
    read_data = f.read().strip().split('\n')
    # Turn first line into list
    moves = eval('[' + read_data[0] + ']')

    # Make list of grids
    grids = []
    grid = []
    row = []
    # Add a checkpoint at the end to make the last grid
    read_data.append('')
    for i in read_data[2:]:
        if i == '':
            grids.append(grid)
            grid = []
            continue
        for j in i.split():
            row.append(int(j))
        grid.append(row)
        row = []

    def bingo(grids, moves):
        drawn = []
        winning_moves = []
        check = 0
        ranking = []
        for m in moves:
            drawn.append(m)
            # Check only when drawn 5 time
            if len(drawn) >= 5:
                #print(ranking)
                for index, g in enumerate(grids):
                    win = False

                    # Check rows
                    for row in g:
                        check = 0
                        for i in row:
                            if i in drawn:
                                check += 1
                                #print(i, check)
                        if check == 5:
                            if index not in ranking:
                                winning_moves.append(m)
                                ranking.append(index)
                            win = True
                            break

                    # Check columns
                    for i in range(len(g[0])):
                        if win:
                            break
                        check = 0
                        for j in range(len(g)):
                            if g[j][i] in drawn:
                                check += 1
                        if check == 5:
                            if index not in ranking:
                                winning_moves.append(m)
                                ranking.append(index)
                            break

        first_win_index = drawn.index(winning_moves[0])
        last_win_index = drawn.index(winning_moves[-1])
        # print(drawn[:last_win_index+1], winning_moves[-1], grids[ranking[-1]])
        # return drawn[:first_win_index+1], winning_moves[0], grids[ranking[0]]
        return drawn[:last_win_index+1], winning_moves[-1], grids[ranking[-1]]

    def final_score(drawn, winning_move, grid):
        not_drawn = []
        # print(drawn)
        for row in grid:
            for i in row:
                #print(i, i in drawn)
                if i not in drawn:
                    not_drawn.append(i)
        # print(sum(not_drawn), not_drawn)
        return sum(not_drawn) * winning_move

    drawn, winning_move, grid = bingo(grids, moves)
    print(final_score(drawn, winning_move, grid))


