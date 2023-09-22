with open('day16.txt') as f:
    read_data = f.read().strip().replace('or ', '').split('\n\n')
    processed_data = [_.split('\n') for _ in read_data]
    print(processed_data)

    fields = {}
    for f in processed_data[0]:
        f = f.split(': ')
        fields[f[0]] = [int(_) for _ in f[1].replace('-', ' ').split()]
    for f, v in fields.items():
        fields[f] = list(range(v[0], v[1] + 1)) + list(range(v[2], v[3] + 1))
    # print(fields)

    ticket = eval('[' + processed_data[1][1] + ']')
    # print(ticket)

    nearby_tickets = []
    for t in range(1, len(processed_data[2])):
        nearby_tickets.append(eval('[' + processed_data[2][t] + ']'))
    # print(nearby_tickets)


class Tickets():
    def __init__(self, fields, ticket, nearby_tickets):
        self.fields = fields
        self.my_ticket = ticket
        self.nearby_tickets = nearby_tickets
        self.invalids = []
        self.ticket = {}

    def main(self):
        # Part 1
        print(sum(self.find_invalid()))
        # Part 2
        for t in self.invalids:
            self.nearby_tickets.remove(t)
        # print(self.nearby_tickets)
        self.complete_ticket()
        print(self.ticket)
        result = 1
        for f in self.ticket:
            if f.startswith('departure'):
                result *= self.ticket[f]
        print(result)

    def find_invalid(self):
        invalid_fields = []
        for t in self.nearby_tickets:
            for v in t:
                if all(v not in f for f in self.fields.values()):
                    self.invalids.append(t)
                    invalid_fields.append(v)
        return invalid_fields

    def complete_ticket(self):
        map = {}
        for i in range(len(self.nearby_tickets[0])):
            map[i] = []
            for f in fields:
                if all(t[i] in fields[f] for t in self.nearby_tickets):
                    map[i].append(f)
        # print(map)
        for _ in range(len(self.fields)):
            for i, f in map.items():
                if len(f) == 1:
                    for j, k in map.items():
                        if f[0] in k and len(k) > 1:
                            map[j].remove(f[0])
        # print(map)
        for i, f in map.items():
            self.ticket[f[0]] = self.my_ticket[i]


t = Tickets(fields, ticket, nearby_tickets)
t.main()
