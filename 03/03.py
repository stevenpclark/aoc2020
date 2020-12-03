import numpy as np

def count_trees(grid, slope):
    dc, dr = slope

    num_trees = 0
    r, c = 0, 0
    nr, nc = grid.shape

    while r < nr:
        if grid[r,c] == '#':
            num_trees += 1
        r += dr
        c = (c+dc)%nc

    return num_trees

def part1(grid):
    print(count_trees(grid, (3, 1)))


def part2(grid):
    slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
    print(np.prod([count_trees(grid, slope) for slope in slopes]))
        

def main():
    with open('input.txt', 'r') as f:
        lines = [list(s.strip()) for s in f.readlines()]
    grid = np.array(lines, dtype=np.chararray)
    part1(grid)
    part2(grid)


if __name__ == '__main__':
    main()
