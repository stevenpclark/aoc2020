from collections import Counter
import numpy as np

def main():
    #fn = 'test.txt'
    fn = 'input.txt'
    with open(fn, 'r') as f:
        vals = [int(s) for s in f.readlines()]
    vals.sort()
    vals.insert(0, 0)
    vals.append(vals[-1]+3)
    counts = Counter(np.diff(vals))
    print(counts[1]*counts[3])

    ways = [0]*len(vals)
    ways[-1] = 1
    for i in range(len(vals)-1,-1,-1):
        v = vals[i]
        for j in range(i+1, i+4):
            if j >= len(vals) or vals[j]-v > 3:
                break
            ways[i] += ways[j]
    print(ways[0])


if __name__ == '__main__':
    main()
