class Solution(object):
    def method(self, x):
        ans = x

        return ans

def main():
    solution = Solution()
    while True:
        try:
            line = input()
        except EOFError:
            break

        nums = list(map(int, line.split()))
        print(solution.method(nums))

if __name__ =="__main__":
    main()
