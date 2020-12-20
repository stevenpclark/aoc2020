from itertools import product
from pprint import pprint

class Node:
    def __init__(self, li):
        ind, rest = li.split(':')
        self.ind = int(ind)
        if '"' in rest:
            self.is_terminal = True
            self.alts = [rest[2]]
        else:
            self.is_terminal = False
            self.alts = list()
            for alt in rest.split(' | '):
                self.alts.append([int(s) for s in alt.split()])

    def solve(self, d):
        #return a list of possible solutions
        #that is, a list of strings
        if self.is_terminal:
            return self.alts
        else:
            solutions = list()
            for alt in self.alts:
                part = d[alt[0]].solve(d)
                #parts should always be a list of strings
                for n in alt[1:]:
                    part = [''.join(p) for p in product(part, d[n].solve(d))]
                solutions.extend(part)
        return solutions

    def can_match(self, msg, d):
        if self.is_terminal:
            return msg == self.alts[0]
        else:
            for alt in self.alts:
                part = d[alt[0]].solve(d)
                #parts should always be a list of strings
                for n in alt[1:]:
                    #remove strings that don't occur at start of msg
                    part = [p for p in part if msg.startswith(p)]
                    if not part:
                        #this alt is a failure
                        break
                    part = [''.join(p) for p in product(part, d[n].solve(d))]
                part = [p for p in part if msg.startswith(p)]
                if part:
                    return True
        return False


if __name__ == '__main__':
    fn = 'input.txt'
    #fn = 'test2.txt'
    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    messages = list()
    d = dict()
    phase = 0
    for li in lines:
        if not li:
            phase = 1
            continue
        if phase == 0:
            node = Node(li)
            d[node.ind] = node
        else:
            messages.append(li)

    allowed = set(d[0].solve(d))
    print(sum([msg in allowed for msg in messages]))


    d[8] = Node('8: 42 | 42 8')
    d[11] = Node('11: 42 31 | 42 11 31')
    #0 = 8 11
    #8 = (42)+
    #11 = N*42, N*31
    #0 = (M+N)*42 N*31    -> M>=1, N>=1
        
    r42 = set(d[42].solve(d))
    r31 = set(d[31].solve(d))

    #42 and 31 are 2 non-intersecting sets of 128 each. strs of len 8
    num_pass = 0
    for msg in messages:
        num_42 = 0
        num_31 = 0
        for i in range(0, len(msg), 8):
            s = msg[i:i+8]
            if s in r42:
                if num_31>0:
                    break #can't have 42 after 31
                num_42 += 1
            else:
                assert s in r31
                num_31 += 1
                if num_31 > num_42:
                    break #invalid
        else:
            if num_31 >= 1 and num_42 > num_31:
                num_pass += 1
    print(num_pass)


