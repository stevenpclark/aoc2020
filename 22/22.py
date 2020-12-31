def part1(d0, d1):
    while d0 and d1:
        c0, c1 = d0.pop(0), d1.pop(0)

        if c0 > c1:
            d0.extend([c0, c1])
        else:
            d1.extend([c1, c0])

    winner = d0 if d0 else d1

    print(sum((i+1)*v for i, v in enumerate(reversed(winner))))


def part2(d0, d1, depth=0):
    #return True if d0 wins, False otherwise
    seen = set()
    while d0 and d1:
        k = tuple(d0)
        if k in seen:
            return True
        seen.add(k)

        c0, c1 = d0.pop(0), d1.pop(0)

        if len(d0) >= c0 and len(d1) >= c1:
            #play a new game, recursively
            d0_wins = part2(d0[:c0], d1[:c1], depth+1)
        else:
            d0_wins = c0 > c1

        if d0_wins:
            d0.extend([c0, c1])
        else:
            d1.extend([c1, c0])

    d0_wins = bool(d0)
    winner = d0 if d0_wins else d1

    if depth==0:
        print(sum((i+1)*v for i, v in enumerate(reversed(winner))))

    return d0_wins


def main(fn):
    d0 = list()
    d1 = list()
    active = d0
    with open(fn, 'r') as f:
        for li in f.read().splitlines():
            if not li:
                active = d1
            else:
                try:
                    active.append(int(li))
                except ValueError:
                    pass

    part1(d0[:], d1[:])
    part2(d0[:], d1[:])


if __name__ == '__main__':
    fn = 'input.txt'
    main(fn)
