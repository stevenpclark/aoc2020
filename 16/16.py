from itertools import permutations
import numpy as np

class Rule:
    def __init__(self, li):
        self.name, rest = li.split(': ')
        ranges = rest.split(' or ')
        ranges = [s.split('-') for s in ranges]
        self.ranges = [(int(x[0]), int(x[1])) for x in ranges]

    def allows(self, v):
        for min_val, max_val in self.ranges:
            if min_val<=v<=max_val:
                return True
        return False

    def init_possible_fields(self, num_fields):
        self.possible_fields = list(range(num_fields))

    def update_possible_fields(self, ticket):
        for i in self.possible_fields[:]:
            if not self.allows(ticket[i]):
                self.possible_fields.remove(i)

    def get_num_possible_fields(self):
        return len(self.possible_fields)

    def get_field_ind(self):
        assert len(self.possible_fields) == 1
        return self.possible_fields[0]

    def steal_field_from(self, other_rules):
        i = self.get_field_ind()
        for r2 in other_rules:
            if (self is not r2) and (i in r2.possible_fields):
                r2.possible_fields.remove(i)


def main():
    fn = 'input.txt'
    #fn = 'test.txt'
    #fn = 'test2.txt'
    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]
    rules = list()
    your_ticket = None
    nearby_tickets = list()
    section = 0
    for li in lines:
        if not li:
            continue
        if 'your ticket' in li:
            num_rules = len(rules)
            section = 1
        elif 'nearby tickets' in li:
            section = 2
        else:
            if section == 0:
                rules.append(Rule(li))
            elif section == 1:
                your_ticket = [int(s) for s in li.split(',')]
                assert len(your_ticket) == num_rules
            else:
                new_ticket = [int(s) for s in li.split(',')]
                assert len(new_ticket) == num_rules
                nearby_tickets.append(new_ticket)

    err_rate = 0
    for ticket in nearby_tickets[:]:
        for v in ticket:
            if not any([r.allows(v) for r in rules]):
                err_rate += v
                nearby_tickets.remove(ticket)
    print(err_rate)

    """Until first 6 rules have just 1 option each,
    loop over each rule, removing field inds from its set
    if a rule gets down to just 1 item in its set, remove that item from
    all other sets"""
    for rule in rules:
        rule.init_possible_fields(num_rules)

    while sum([rule.get_num_possible_fields() for rule in rules[:6]]) > 6:
        for rule in rules:
            if rule.get_num_possible_fields() <= 1:
                rule.steal_field_from(rules)
                continue
            for ticket in nearby_tickets:
                rule.update_possible_fields(ticket)
                if rule.get_num_possible_fields() <= 1:
                    rule.steal_field_from(rules)
                    break

    print(np.product([your_ticket[r.get_field_ind()] for r in rules[:6]]))


if __name__ == '__main__':
    main()
