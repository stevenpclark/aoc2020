from collections import defaultdict

def main():
    d = defaultdict(list)
    with open('input.txt', 'r') as f:
        s = f.read()
    s = s.replace(' bags', '').replace(' bag', '').replace('.', '')
    for li in s.split('\n'):
        if li:
            left, right = li.split(' contain ')
            links = right.split(', ')
            for link in links:
                try:
                    sn, sa, sb = link.split(' ')
                    d[left].append((int(sn), sa+' '+sb))
                except ValueError:
                    d[left] = list()

    n = 0
    for c in d.keys():
        if can_contain_target(c, d):
            n += 1
    print(n)

    print(count_contents('shiny gold', d))


def can_contain_target(c, d):
    contents = d[c]
    if not contents:
        return False
    if 'shiny gold' in [t[1] for t in contents]:
        return True
    for n, c2 in contents:
        if can_contain_target(c2, d):
            return True
    else:
        return False


def count_contents(c, d):
    contents = d[c]
    total = 0
    for n, c2 in contents:
        total += n*(1+count_contents(c2, d))
    return total


if __name__ == '__main__':
    main()
