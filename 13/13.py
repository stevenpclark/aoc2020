import numpy as np

def part1(t, fields):
    in_service = [int(f) for f in fields if f != 'x']

    choices = sorted([(b-(t%b), b) for b in in_service])
    best = choices[0]
    print(best[0]*best[1])


def part2(fields):
    inds = range(len(fields))
    tups = [(int(p[0]), p[1]) for p in zip(fields, inds) if p[0] != 'x']
    dt, start = tups[0]
    for p in tups[1:]:
        start, dt = get_next(start, dt, p[0], p[1])
    print(start)


def get_next(start, dt, dt2, ind2):
    t = start
    while True:
        if t%dt2 == dt2-(ind2%dt2):
            break
        t += dt
    return t, dt*dt2


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        li1, li2 = f.readlines()
    t = int(li1)
    fields = li2.split(',')
    part1(t, fields)
    part2(fields)

