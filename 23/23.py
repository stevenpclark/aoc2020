class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def main(s, is_part2=False):
    vals = [int(c) for c in s]
    if is_part2:
        num_iters = int(10e6)
        vals.extend(range(max(vals)+1, int(1e6)+1))
    else:
        num_iters = 100

    min_val, max_val = min(vals), max(vals)

    nodes = [Node(v) for v in vals]
    num_nodes = len(nodes)
    node_lookup = dict(zip(vals, nodes))

    for i, node in enumerate(nodes):
        node.next = nodes[(i+1)%num_nodes]

    curr = nodes[0]

    for i in range(num_iters):
        #print('move %d'%(i+1))
        #print([x+1 for x in a])
        #print('parens:', curr_val+1)

        up = [curr.next]
        up.append(up[-1].next)
        up.append(up[-1].next)
        curr.next = up[-1].next
        #print('pick up: %s'%[x+1 for x in up])

        up_vals = [n.val for n in up]
        dest_val = curr.val - 1
        while True:
            if dest_val <= 0:
                dest_val = max_val
            if dest_val not in up_vals:
                break
            dest_val -= 1
        dest = node_lookup[dest_val]

        up[-1].next = dest.next
        dest.next = up[0]

        curr = curr.next

    one = node_lookup[1]
    if not is_part2:
        node = one.next
        ans = list()
        while node != one:
            ans.append(node.val)
            node = node.next
        print(''.join([str(a) for a in ans]))
    else:
        print(one.next.val * one.next.next.val)

if __name__ == '__main__':
    #s = '389125467'
    s = '784235916'

    main(s)
    main(s, is_part2=True)
