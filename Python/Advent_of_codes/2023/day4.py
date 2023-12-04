with open('day4.txt') as f:
    read_data = f.read().strip().split('\n')
    cards = [i.split(': ')[1].split(' | ') for i in read_data]
    cards = [[i.split() for i in j] for j in cards]


def count_win_nums(card):
    win = 0
    for winning_nums in card[0]:
        if winning_nums in card[1]:
            win += 1
    return win


def map_winning_amount():      # {card_id: amount of winning numbers}
    m_dict = {}
    for i in range(len(cards)):
        m = count_win_nums(cards[i])
        if m > 0:
            m_dict[i] = m
    return m_dict


win_dict = map_winning_amount()
card_pile = {i: 1 for i in range(len(cards))}

total_points = 0
for c in win_dict:
    win_amount = win_dict[c]
    total_points += 2 ** (win_amount - 1)
    for i in range(win_amount):
        card_pile[c + i + 1] += card_pile[c]    # exp: 3 cards x -> 3 x (cards y, z ) + old amount of cards y, z

print(total_points)
print(sum(v for v in card_pile.values()))

