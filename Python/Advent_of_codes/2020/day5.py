with open('day5.txt') as f:
    read_data = f.read().strip().split('\n')
    pos = [[i[:-3], i[-3:]] for i in read_data]


def find_seat(pos):
    seats = []
    for p in pos:
        rows = list(range(128))
        cols = list(range(8))
        for i in p[0]:
            if i == 'F':
                rows = rows[:len(rows) // 2]
            else:
                rows = rows[len(rows) // 2:]
        for i in p[1]:
            if i == 'L':
                cols = cols[:len(cols) // 2]
            else:
                cols = cols[len(cols) // 2:]
        seats.append((rows[0], cols[0]))
    return seats


# Part 1
seats = find_seat(pos)
def find_id(seats):
    seat_ids = []
    for seat in seats:
        id = seat[0]*8 + seat[1]
        seat_ids.append(id)
    return seat_ids

seat_ids = find_id(seats)
print(max(seat_ids))

# Part 2
for col in range(8):
    for row in range(1, 127):
        if (row, col) not in seats:
            id = find_id([(row, col)])
            if id[0] + 1 in seat_ids and id[0] - 1 in seat_ids:
                print(id)