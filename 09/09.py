from itertools import combinations

def main():
    with open('input.txt', 'r') as f:
        nums = [int(s) for s in f.readlines()]

    N = 25
    invalid_num = None
    for i in range(N, len(nums)):
        pairs = combinations(nums[i-N:i], 2)
        for a,b in pairs:
            if a+b == nums[i]:
                break
        else:
            invalid_num = nums[i]

    print(invalid_num)

    found_window = None

    for window_size in range(2, len(nums)-1):
        for i in range(window_size-1, len(nums)):
            window = nums[i-window_size+1:i+1]
            if sum(window) == invalid_num:
                found_window = window
                break
        if found_window:
            break

    print(min(found_window) + max(found_window))


if __name__ == '__main__':
    main()
