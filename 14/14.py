import itertools

def apply_mask(v, mask):
    set_mask = int(mask.replace('X', '0'), 2)
    clear_mask = int(mask.replace('1', 'X').replace('0', '1').replace('X', '0'), 2)
    v |= set_mask
    v &= ~clear_mask
    return v


def part1(cmds, use_direct_mode=True):
    arr = dict()
    mask = None

    for c, v in cmds:
        if c == 'mask':
            mask = v
        else:
            addr = int(c[4:-1])
            if use_direct_mode:
                arr[addr] = apply_mask(int(v), mask)
            else:
                addr_list = list(bin(addr)[2:].zfill(36))
                for i, m in enumerate(mask):
                    if m == '0':
                        continue
                    addr_list[i] = m
                x_inds = [i for i, c in enumerate(addr_list) if c=='X']
                num_x = len(x_inds)
                for bits in itertools.product(['0','1'], repeat=num_x):
                    for x_ind, x_val in zip(x_inds, bits):
                        addr_list[x_ind] = x_val
                    arr[int(''.join(addr_list), 2)] = int(v)
    print(sum(arr.values()))


def main():
    with open('input.txt', 'r') as f:
        cmds = [li.rstrip().split(' = ') for li in f.readlines()]
    part1(cmds)
    part1(cmds, use_direct_mode=False)


if __name__ == '__main__':
    main()
