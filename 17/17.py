import numpy as np
from scipy import ndimage

def main(grid, ndim=3):
    kern = np.ones([3]*ndim,dtype=np.uint8)
    kern[(1,)*ndim] = 0

    for i in range(6):
        grid = np.pad(grid, 1)
        counts = ndimage.convolve(grid, kern, mode='constant', cval=0)
        for ind, v in np.ndenumerate(grid):
            n = counts[ind]
            if v == 1 and n not in [2,3]:
                grid[ind] = 0
            elif v == 0 and n == 3:
                grid[ind] = 1
    print(np.sum(grid))
    
if __name__ == '__main__':
    #fn = 'test.txt'
    fn = 'input.txt'
    with open(fn, 'r') as f:
        lines = [[c=='#' for c in li.strip()] for li in f.readlines()]
    grid = np.array(lines, dtype=np.uint8)[:,:,np.newaxis]
    main(grid)

    grid = np.array(lines, dtype=np.uint8)[:,:,np.newaxis, np.newaxis]
    main(grid, ndim=4)
