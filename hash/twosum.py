import sys


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return seen[need], i
        seen[num] = i
    return -1, -1


def parse_input(data):
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return [], 0

    first_line = list(map(int, lines[0].split()))
    values = list(map(int, data.split()))

    if len(first_line) >= 2:
        n, target = first_line[0], first_line[1]
        nums = values[2 : 2 + n]
        return nums, target

    n = first_line[0]
    rest = values[1:]
    if len(rest) >= n + 1:
        nums = rest[:n]
        target = rest[n]
        return nums, target

    raise ValueError("Invalid input")


def main():
    nums, target = parse_input(sys.stdin.read())
    i, j = two_sum(nums, target)
    print(i, j)


if __name__ == "__main__":
    main()
