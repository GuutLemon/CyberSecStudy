from collections import defaultdict, Counter

with open('day4.txt') as f:
    read_data = sorted(f.read().strip().replace('#', '').split('\n'))
    processed_data = [[i[1:i.find('] ')], i[i.find('] ') + 2:]] for i in read_data]
    print(processed_data)


class Guard:
    def __init__(self, data):
        self.data = data
        self.guards = defaultdict(list)

    def main(self):
        self.count_sleep_time()
        print(self.find_most_sleep())
        print(self.find_most_sleep_minute())

    def count_sleep_time(self):
        current_guard = ''
        start = 0
        for i in self.data:
            note = i[1]
            time = i[0]
            if note.startswith('G'):
                note = note.split()
                current_guard = note[1]
            elif note.startswith('f'):
                start = int(time[-2:])
            else:
                end = int(time[-2:])
                self.guards[current_guard].extend(range(start, end))
                start = 0

    def find_most_sleep(self):
        for g in self.guards:
            if len(self.guards[g]) == max([len(m) for m in self.guards.values()]):
                most_sleep_guard = g
                break
        minutes = Counter(self.guards[most_sleep_guard])
        for m in minutes:
            if minutes[m] == max([counter for counter in minutes.values()]):
                most_sleep_minute = m
                break
        return int(most_sleep_guard) * most_sleep_minute

    def find_most_sleep_minute(self):
        sleep_counter = {}
        for g, m in self.guards.items():
            sleep_counter[g] = Counter(m)
        max_count = max([max(j.values()) for j in sleep_counter.values()])
        for g, counter in sleep_counter.items():
            if max(counter.values()) == max_count:
                for m in counter:
                    if counter[m] == max_count:
                        return int(g) * m


if __name__ == '__main__':
    g = Guard(processed_data)
    g.main()

