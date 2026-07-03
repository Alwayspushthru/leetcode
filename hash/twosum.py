import sys

def solve(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return seen[need], i
        seen[num] = i

def main():
    lines = sys.stdin.read().splitlines()
    nums = list(map(int, lines[0].split()))
    target = int(lines[1])

    i, j = solve(nums, target)
    print(i, j)


if __name__ == "__main__":
    main() 
