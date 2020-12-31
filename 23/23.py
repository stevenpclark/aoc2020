def main():
    N = 9
    a = [x-1 for x in [3,8,9,1,2,5,4,6,7]]
    curr_ind = 0

    for i in range(5):
        print('move %d'%(i+1))
        print([x+1 for x in a])
        curr_val = a[curr_ind]
        print(curr_val+1)

        up = []
        up.append(a.pop((curr_ind+1)%len(a)))
        up.append(a.pop((curr_ind+1)%len(a)))
        up.append(a.pop((curr_ind+1)%len(a)))
        print('pick up: %s'%[x+1 for x in up])
        dest_val = curr_val

        while True:
            dest_val = (dest_val-1)%N
            if dest_val not in up:
                break
        print('destination: %d'%(dest_val+1))
        print()
        dest_ind = a.index(dest_val)
        a[dest_ind+1:dest_ind+1] = up
        curr_ind = (curr_ind+1)%N

if __name__ == '__main__':
    main()
