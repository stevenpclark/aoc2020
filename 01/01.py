from itertools import combinations

def part1(numbers):
    for a, b in combinations(numbers, 2):
        if a+b == 2020:
            print(a*b)

def part2(numbers):
    for a, b, c in combinations(numbers, 3):
        if a+b+c == 2020:
            print(a*b*c)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        numbers = [int(li) for li in f]
    part1(numbers)
    part2(numbers)
