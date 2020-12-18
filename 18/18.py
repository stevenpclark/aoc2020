from operator import add, mul

def process_line(li):
    li = list(li.strip().replace(' ', ''))
    for i, c in enumerate(li):
        if c not in '*+()':
            li[i] = int(c)
    return li


def augment_line(li):
    i = len(li)-1
    while i >= 0:
        x1 = li[i] 
        if x1 == '+':
            p_depth = 0
            for j in range(i+1,len(li)):
                x2 = li[j]
                if x2 == '(':
                    p_depth += 1
                elif x2 == ')':
                    p_depth -= 1
                if p_depth == 0:
                    li.insert(j+1, ')')
                    break
            for j in range(i-1,-1,-1):
                x2 = li[j]
                if x2 == ')':
                    p_depth += 1
                elif x2 == '(':
                    p_depth -= 1
                if p_depth == 0:
                    li.insert(j, '(')
                    break
        i -= 1
    return li
            

def solve(li):
    assert type(li[0])==int or li[0]=='('
    r = None
    op = None
    i = 0
    while i < len(li):
        x = li[i]
        v = None
        if x == ')':
            return r, i+1
        elif x == '(':
            v, n = solve(li[i+1:])
            i += n
        elif x == '+':
            op = add
        elif x == '*':
            op = mul
        else:
            v = x
        if v is not None:
            if r is None:
                r = v
            else:
                r = op(r, v)
        i += 1
    return r, len(li)


def main():
    fn = 'input.txt'
    #fn = 'test1.txt'
    with open(fn, 'r') as f:
        lines = [process_line(li) for li in f.readlines()]

    print(sum([solve(li)[0] for li in lines]))

    print(sum([solve(augment_line(li))[0] for li in lines]))


if __name__ == '__main__':
    main()
