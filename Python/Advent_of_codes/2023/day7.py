import re
from collections import Counter

with open('day7.txt') as f:
    read_data = f.read().strip().split('\n')

hands = {i.split()[0]: int(i.split()[1]) for i in read_data}
# strength = '23456789TJQKA'
strength = 'J23456789TQKA'


class HandsSorting:
    def __init__(self, hands, strength):
        self.hands = hands
        self.strength = strength
        self.types = {'0': [], '1': [], '2': [], '3': [], '3.2': [], '4': [], '5': []}

    def solve(self):
        s = self.sorted_hands()
        result = 0
        for i in range(len(s)):
            result += hands[s[i]] * (i + 1)
        print(result)

    def sorted_hands(self):
        self.sort_by_types()
        self.sort_by_strength()
        sorted_hands = []
        for t in self.types:
            for h in self.types[t]:
                sorted_hands.append(h)
        return sorted_hands

    # Part 1
    # def sort_by_types(self):
    #     for hand in self.hands:
    #         p = r'(.)\1*'
    #         matches = list(set(re.findall(p, hand)))
    #         l = len(matches)
    #         self.sort_to_type(hand, matches, len_matches)
    # Should've rewritten all of this

    def sort_to_type(self, hand, matches, len_matches):
        if len_matches == 1:
            self.types['5'].append(hand)
        elif len_matches == 2:
            if hand.count(matches[0]) == 4 or hand.count(matches[0]) == 1:
                self.types['4'].append(hand)
            else:
                self.types['3.2'].append(hand)
        elif len_matches == 3:
            if any(hand.count(matches[i]) == 3 for i in range(3)):
                self.types['3'].append(hand)
            else:
                self.types['2'].append(hand)
        elif len_matches == 4:
            self.types['1'].append(hand)
        else:
            self.types['0'].append(hand)

    def sort_by_types(self):
        for hand in self.hands:
            if 'J' in hand and hand != 'JJJJJ':     # Either do this or have to check when j > other words
                words_count = Counter(hand.replace('J', ''))
                most_word = max(words_count.values())
                j = hand.count('J')
                if j + most_word == 5:
                    self.types['5'].append(hand)
                elif j + most_word == 4:
                    self.types['4'].append(hand)
                elif j + most_word == 3:
                    if list(words_count.values()) == [2, 2] and j == 1:
                        self.types['3.2'].append(hand)
                    else:
                        self.types['3'].append(hand)
                # No 2 pairs with J
                elif j + most_word == 2:
                    self.types['1'].append(hand)
            # Back to part 1 for leftover
            else:
                words_count = Counter(hand)
                m = list(words_count.keys())
                l = len(m)
                self.sort_to_type(hand, m, l)

    def sort_by_strength(self):
        for type in self.types:
            t = self.types[type]
            if len(t) > 1:
                for i in range(len(t)):
                    for j in range(0, len(t) - i - 1):
                        # Check deeper for 'AAK', 'AAJ'
                        for k in range(len(t[j])):
                            current = t[j][k]
                            next = t[j + 1][k]
                            if self.strength.index(current) > self.strength.index(next):
                                t[j], t[j + 1] = t[j + 1], t[j]
                                break
                            elif self.strength.index(current) < self.strength.index(next):
                                break


a = HandsSorting(hands, strength)
a.solve()