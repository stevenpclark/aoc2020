def main(fn):
    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]
    cmds = list()
    for li in lines:
        fields = li.split()
        cmds.append([fields[0], int(fields[1])])

    is_looping, acc = run(cmds)
    print(acc)

    for i in range(len(cmds)):
        if not flip_cmd(cmds[i]):
            continue
        is_looping, acc = run(cmds)
        if not is_looping:
            print(acc)
            break
        flip_cmd(cmds[i])


def flip_cmd(cmd):
    if cmd[0] == 'nop':
        cmd[0] = 'jmp'
    elif cmd[0] == 'jmp':
        cmd[0] = 'nop'
    else:
        return False
    return True


def run(cmds):
    acc = 0
    pc = 0
    visited = set()
    is_looping = False
    while pc != len(cmds):
        if pc in visited:
            is_looping = True
            break
        visited.add(pc)

        cmd, val = cmds[pc]

        if cmd == 'nop':
            pc += 1
        elif cmd == 'acc':
            acc += val
            pc += 1
        elif cmd == 'jmp':
            pc += val
        else:
            raise ValueError
    return is_looping, acc

if __name__ == '__main__':
    fn = 'input.txt'
    #fn = 'test.txt'
    main(fn)
