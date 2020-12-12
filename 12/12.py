DP_MAP = {'N':(0,1), 'S':(0,-1), 'E':(1,0), 'W':(-1,0)}
FLIP_TURN = {'L':'R', 'R':'L'}

def turn(dp, c, v):
    dx, dy = dp
    if v == 180:
        return (-dx, -dy)
    if v == 270:
        v = 90
        c = FLIP_TURN[c]

    if c == 'R':
        return (dy, -dx)
    else:
        return (-dy, dx)


def main(dp=(1,0), use_waypoint=False):
    fn = 'input.txt'
    with open(fn, 'r') as f:
        cmds = [(s[0], int(s[1:])) for s in f.readlines()]
    x, y = 0, 0
    for c, v in cmds:
        if c in ['L', 'R']:
            dp = turn(dp, c, v)
            continue
        if c == 'F':
            x += v*dp[0]
            y += v*dp[1]
            continue
        dx, dy = DP_MAP[c]
        if not use_waypoint:
            x += v*dx
            y += v*dy
        else:
            dp = (dp[0]+v*dx, dp[1]+v*dy)

    print(abs(x)+abs(y))
            

if __name__ == '__main__':
    main()
    main(dp=(10,1), use_waypoint=True)
