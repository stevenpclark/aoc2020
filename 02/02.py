def parse_line(li):
    a, c, password = li.split(' ')
    a1, a2 = a.split('-')
    c = c[0]
    lower = int(a1)
    upper = int(a2)
    return lower, upper, c, password

def is_valid1(lower, upper, c, password):
    return lower <= password.count(c) <= upper

def is_valid2(lower, upper, c, password):
    return (password[lower-1] == c) ^ (password[upper-1] == c)

def part1(lines, checker_func):
    num_valid = 0
    for li in lines:
        lower, upper, c, password = parse_line(li)
        if checker_func(lower, upper, c, password):
            num_valid += 1
    print(num_valid)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    part1(lines, is_valid1)
    part1(lines, is_valid2)
