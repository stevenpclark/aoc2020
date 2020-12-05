REMAP_ROW = {'F':'0', 'B':'1'}
REMAP_COL = {'L':'0', 'R':'1'}

def get_row_col(s):
    s_r = s[:7]
    s_c = s[7:]
    for k,v in REMAP_ROW.items():
        s_r = s_r.replace(k, v)
    for k,v in REMAP_COL.items():
        s_c = s_c.replace(k, v)
    return int(s_r, 2), int(s_c, 2)

def get_seat_id(s):
    r, c = get_row_col(s)
    return r*8 + c


def get_seat_ids(lines):
    return [get_seat_id(s) for s in lines]


def main():
    with open('input.txt', 'r') as f:
        lines = [s.strip() for s in f.readlines()]
    seat_ids = get_seat_ids(lines)
    print(max(seat_ids))
    seat_ids.sort()
    for i, s_id in enumerate(seat_ids[1:]):
        expected = seat_ids[i]+1
        if s_id != expected:
            print(expected)

if __name__ == '__main__':
    main()
