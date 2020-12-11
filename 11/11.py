import sys
from copy import deepcopy
import numpy as np

DIRS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def count_occupied_neighbors(grid, r, c, nr, nc, extend=False):
    num_occupied = 0
    for dr, dc in DIRS:
        r2, c2 = r, c
        while True:
            r2 += dr
            c2 += dc
            if r2<0 or r2>=nr or c2<0 or c2>=nc:
                break
            v = grid[r2, c2]
            if v == 'L':
                break
            if v == '#':
                num_occupied += 1
                break
            if not extend:
                break
    return num_occupied


def part1(grid, threshold, extend):
    nr, nc = grid.shape

    modified = True
    while modified:
        #print()
        #np.savetxt(sys.stdout.buffer, grid, fmt='%s', delimiter='')
        next_grid = deepcopy(grid)
        modified = False
        for (r,c), v in np.ndenumerate(grid):
            if grid[r,c] == '.':
                continue
            n = count_occupied_neighbors(grid, r, c, nr, nc, extend)
            if v == 'L':
                if n == 0:
                    next_grid[r,c] = '#'
                    modified = True
            else:
                if n >= threshold:
                    next_grid[r,c] = 'L'
                    modified = True
        grid = next_grid
    unique, counts = np.unique(grid, return_counts=True)
    counts = dict(zip(unique, counts))
    print(counts['#'])

def main():
    with open('input.txt', 'r') as f:
        lines = [list(s.strip()) for s in f.readlines()]
    grid = np.array(lines, dtype=np.chararray)
    part1(grid, 4, extend=False)
    part1(grid, 5, extend=True)


if __name__ == '__main__':
    main()
