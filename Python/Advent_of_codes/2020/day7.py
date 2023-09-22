with open('day7.txt') as f:
    read_data = f.read().strip().replace(' bags contain ', '/').replace(' bag, ', '/').replace(' bags.', '').replace(' bags, ', '/').replace(' bag.', '').split('\n')
    print(read_data)

bags = {}
for b in read_data:
    b = b.split('/')
    bags[b[0]] = b[1:]
print(bags)


class Goldbag():
    def __init__(self, bags):
        self.bags = bags
        self.gold_bags = ['shiny gold']

    def main(self):
        result1 = self.find_gold_bags()
        print(len(result1[1:]))
        result2 = self.inside('shiny gold')
        print(result2)

    # Part 1
    def find_gold_bags(self, check=0, l=0):
        while True:
            for n in self.gold_bags[-l:]:   # Only check newly added
                new_bags = []
                for b, v in bags.items():
                    for i in v:
                        if i[2:] == n and b not in self.gold_bags:
                            new_bags.append(b)
                check += len(new_bags)
                #print(new_bags)
                self.gold_bags.extend(new_bags)
            if check == 0:      # All new_bags are empty
                return self.gold_bags
            l = check
            check = 0

    # Part 2
    def inside(self, check):
        count = 0
        # print(self.bags[check])
        for v in self.bags[check]:
            if v[0].isdigit():
                count += int(v[0]) * self.inside(v[2:]) + int(v[0])
                # print(v, count)
        return count


g = Goldbag(bags)
g.main()