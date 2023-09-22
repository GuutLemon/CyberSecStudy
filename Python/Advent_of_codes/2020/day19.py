with open('day19.txt') as f:
    # read_data = f.read().strip().replace('"', '').split('\n\n')   # Part 1
    read_data = f.read().strip().replace('"', '').split('\n\n')
    rules = {i.split(': ')[0]: i.split(': ')[1].split(' | ') if '|' in i.split(': ')[1] else [i.split(': ')[1]] for i in read_data[0].split('\n')}
    print(rules)
    messages = read_data[1].split('\n')
    # print(messages)


class CheckMessages():
    def __init__(self, rules, messages):
        self.rules = rules
        self.messages = messages
        self.completed_rules = {i: None for i in self.rules}
        self.loop_rules = {}
        # Part 2
        for i, v in list(self.rules.items()):
            if i == '8' or i == '11' or not all('8' not in i.split() for i in v) or not all('11' not in i.split() for i in v):
                self.loop_rules[i] = v
                del self.rules[i]
                del self.completed_rules[i]


    def main(self):
        valid = []
        self.make_rule()
        self.make_rule2()
        print(self.completed_rules['11'])
        for m in self.messages:
            if m in self.completed_rules['0']:
                valid.append(m)
        print(len(valid))

    def make_rule(self):
        while not all(v for v in self.completed_rules.values()):
            for r, v in self.rules.items():
                # print(self.completed_rules[r])
                if self.completed_rules[r]:
                    continue
                elif v[0] == 'a' or v[0] == 'b':
                    self.completed_rules[r] = v[0]
                elif not all(self.completed_rules[i] for j in v for i in j.split()):
                    continue
                else:
                    self.completed_rules[r] = []
                    for i in v:
                        to_sum = []
                        for j in i.split():
                            to_sum.append(self.completed_rules[j])
                        self.completed_rules[r].extend(list(self.sum_rules(to_sum)))

    def sum_rules(self, lists):
        if len(lists) == 1:
            yield from lists[0]
        else:
            for i in lists[0]:
                for j in self.sum_rules(lists[1:]):
                    yield i + j

    def sum_looped_rules(self, r, lists):
        max_len = max([len(_) for _ in self.messages])
        if len(lists) == 1:
            yield from lists[0]
        elif not all(len(i) <= max_len for i in self.completed_rules[r]):
            print('DOG')
            yield from lists
        else:
            print('DDDD', r)
            # print(self.completed_rules[r])
            for i in lists[0]:
                for j in self.sum_looped_rules(r, lists[1:]):
                    yield i + j

    def make_rule2(self):
        self.rules.update(self.loop_rules)
        self.completed_rules.update({i: None for i in self.loop_rules})
        max_len = max([len(_) for _ in self.messages])
        while not all(v for v in self.completed_rules.values()):
            for r, v in self.rules.items():
                # print(self.completed_rules[r])
                if self.completed_rules[r]:
                    continue
                elif r == '0' and not all(self.completed_rules[i] for j in v for i in j.split()):
                    continue
                else:
                    self.completed_rules[r] = []
                    if r == '8' or r == '11':
                        while all(len(i) <= max_len for i in self.completed_rules[r]):
                            for i in v:
                                to_sum = []
                                for j in i.split():
                                    to_sum.append(self.completed_rules[j])
                                if r == '8' or r == '11':
                                    self.completed_rules[r].extend(list(self.sum_rules(to_sum)))
                    else:
                        for i in v:
                            to_sum = []
                            for j in i.split():
                                to_sum.append(self.completed_rules[j])
                            self.completed_rules[r].extend(list(self.sum_rules(to_sum)))

c = CheckMessages(rules, messages)
c.main()