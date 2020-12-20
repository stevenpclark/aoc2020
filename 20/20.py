import time
from copy import deepcopy
import numpy as np
from scipy import ndimage

TILE_SZ = 10
WORLD_SZ = 12

def get_grid_variants(grid):
    nr, nc = grid.shape
    variants = np.zeros((8, nr, nc), dtype=np.uint8)
    for i in range(4):
        variants[i*2,:,:] = grid
        variants[i*2+1,:,:] = np.fliplr(grid)
        grid = np.rot90(grid)
    return variants


class Tile:
    def __init__(self, lines):
        self.tile_id = int(lines[0].split()[-1][:-1])
        grid = [[c=='#' for c in li] for li in lines[1:]]
        grid = np.array(grid, dtype=np.uint8)
        assert grid.shape == (TILE_SZ, TILE_SZ)
        self.grids = get_grid_variants(grid)


    def get_variant(self, i):
        return self.grids[i,:,:]

    def get_content(self, i):
        return self.grids[i,1:-1,1:-1]

    def get_possible_variants(self, world, r, c):
        #world is a 2-d array of (tile, var_ind) (or (None, None))
        #return a list of ints, corresponding to possible variants that fit
        possible = list(range(8))
        for i in possible[:]:
            if r > 0: #compare with north
                other_tile, other_var = world[r-1][c]
                if other_tile:
                    other = other_tile.get_variant(other_var)
                    if not np.array_equal(other[-1,:], self.grids[i,0,:]):
                        possible.remove(i)
                        continue
            if r < WORLD_SZ-1: #compare with south
                other_tile, other_var = world[r+1][c]
                if other_tile:
                    other = other_tile.get_variant(other_var)
                    if not np.array_equal(other[0,:], self.grids[i,-1,:]):
                        possible.remove(i)
                        continue

            if c > 0: #compare with west
                other_tile, other_var = world[r][c-1]
                if other_tile:
                    other = other_tile.get_variant(other_var)
                    if not np.array_equal(other[:,-1], self.grids[i,:,0]):
                        possible.remove(i)
                        continue
            if c < WORLD_SZ-1: #compare with east
                other_tile, other_var = world[r][c+1]
                if other_tile:
                    other = other_tile.get_variant(other_var)
                    if not np.array_equal(other[:,0], self.grids[i,:,-1]):
                        possible.remove(i)
                        continue
        return possible

def solve(world, remaining_tiles, r, c):

    if c<WORLD_SZ-1:
        next_r = r
        next_c = c+1
    else:
        next_r = r+1
        next_c = 0
    next_world = deepcopy(world)

    for tile in remaining_tiles:
        possible_vars = tile.get_possible_variants(world, r, c)
        if possible_vars:
            next_tiles = remaining_tiles[:]
            next_tiles.remove(tile)
            for var in possible_vars:
                next_world[r][c] = (tile, var)
                if not next_tiles:
                    return next_world #solved!
                solution = solve(next_world, next_tiles, next_r, next_c)
                if solution:
                    return solution
    return None

def get_monster_template():
    with open('monster.txt', 'r') as f:
        lines = f.read().splitlines()
    template = np.array([[c=='#' for c in li] for li in lines], dtype=np.uint8)
    return template


def get_sea_roughness(initial_grid, monster_template):
    flipped_template = np.rot90(monster_template, 2)
    m_nr, m_nc = monster_template.shape
    m_roff = m_nr//2
    m_coff = m_nc//2 - 1 #fudge factor due to not being an even number

    grids = get_grid_variants(initial_grid)
    for var in range(8):
        grid = grids[var,:,:]
        max_count = np.sum(monster_template)
        matches = ndimage.convolve(grid, flipped_template, mode='constant', cval=0) == max_count
        num_matches = np.sum(matches)
        if num_matches:
            #print(matches.astype(np.uint8))
            locations = np.argwhere(matches) - [m_roff, m_coff]

            test = np.zeros(grid.shape, dtype=np.uint8)
            for r,c in locations:
                grid[r:r+m_nr,c:c+m_nc] -= monster_template
            return np.sum(grid)


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    tiles = list()
    for i in range(0, len(lines), TILE_SZ+2):
        tiles.append(Tile(lines[i:i+TILE_SZ+1]))

    world = [[(tiles[0], 0), (tiles[1], 0)], [(tiles[2], 0), (tiles[3], 0)]]


    num_tiles = len(tiles)

    #144 tiles, so presumably 12x12
    world = [[(None, None) for i in range(WORLD_SZ)] for j in range(WORLD_SZ)]

    t1 = time.time()
    solution = solve(world, tiles, 0, 0)
    corners = list()
    corners.append(solution[0][0][0])
    corners.append(solution[-1][0][0])
    corners.append(solution[0][-1][0])
    corners.append(solution[-1][-1][0])
    print(np.product([tile.tile_id for tile in corners]))
    t2 = time.time()
    content = [[t[0].get_content(t[1]) for t in row] for row in solution]
    solution_grid = np.block(content)

    monster_template = get_monster_template()

    print(get_sea_roughness(solution_grid, monster_template))
    t3 = time.time()

    print(t2-t1, t3-t2)


if __name__ == '__main__':
    main()
