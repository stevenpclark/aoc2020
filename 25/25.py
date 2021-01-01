DIVISOR = 20201227

def transform(subject, loop_size):
    x = 1
    for ls in range(loop_size):
        x *= subject
        x = x%DIVISOR
    return x

def main():
    subject = 7
    public1 = 10705932
    public2 = 12301431
    #public1 = 5764801
    #public2 = 17807724


    x = 1
    ls = 1
    while True:
        x *= subject
        x = x%DIVISOR
        if x == public1:
            print(ls)
            print(transform(public2, ls))
            break
        if x == public2:
            print(ls)
            print(transform(public1, ls))
            break
        ls += 1

if __name__ == '__main__':
    main()
