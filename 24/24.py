from copy import deepcopy
import numpy as np
from scipy import ndimage

SZ = 200
OFF = SZ//2
NEIGHBORS = ((1,0), (1,-1), (0,-1), (-1,0), (-1,1), (0,1))

def chunk_line(s):
    r = list()
    i = 0
    while i < len(s):
        if s[i] in ['e', 'w']:
            r.append(s[i])
            i += 1
        else:
            r.append(s[i:i+2])
            i += 2
    return r


def main():
    fn = 'input.txt'
    with open(fn, 'r') as f:
        lines = [chunk_line(li) for li in f.read().splitlines()]

    blacks = set()

    for li in lines:
        p = [0,0,0]
        for dp in li:
            if dp == 'e':
                p[0] += 1
                p[1] -= 1
            elif dp == 'w':
                p[0] -= 1
                p[1] += 1
            elif dp == 'se':
                p[1] -= 1
                p[2] += 1
            elif dp == 'nw':
                p[1] += 1
                p[2] -= 1
            elif dp == 'ne':
                p[0] += 1
                p[2] -= 1
            else:
                p[0] -= 1
                p[2] += 1
        k = tuple(p)
        if k in blacks:
            blacks.remove(k)
        else:
            blacks.add(k)
    print(len(blacks))

    grid = np.zeros((SZ, SZ), dtype=np.uint8)

    for x,y,z in blacks:
        grid[x+OFF,z+OFF] = 1
    print(np.sum(grid))

    kern = np.zeros((3,3), dtype=np.uint8)
    kern[2,1] = 1
    kern[2,0] = 1
    kern[1,0] = 1
    kern[0,1] = 1
    kern[0,2] = 1
    kern[1,2] = 1

    for i in range(100):
        adj_count = ndimage.convolve(grid, kern, mode='constant', cval=0)
        for (r,c),is_black in np.ndenumerate(grid):
            num_black_neighbors = adj_count[r,c]
            if is_black:
                if num_black_neighbors == 0 or num_black_neighbors > 2:
                    grid[r,c] = 0
            else:
                if num_black_neighbors == 2:
                    grid[r,c] = 1
    print(np.sum(grid))


if __name__ == '__main__':
    main()
