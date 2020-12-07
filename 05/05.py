REMAP = {'F':'0', 'B':'1', 'L':'0', 'R':'1'}

def get_seat_id(s):
    for k,v in REMAP.items():
        s = s.replace(k, v)
    return int(s, 2)

def main():
    with open('input.txt', 'r') as f:
        lines = [s.strip() for s in f.readlines()]
    seat_ids = [get_seat_id(s) for s in lines]
    print(max(seat_ids))
    seat_ids.sort()
    for i, s_id in enumerate(seat_ids[1:]):
        expected = seat_ids[i]+1
        if s_id != expected:
            print(expected)

if __name__ == '__main__':
    main()
