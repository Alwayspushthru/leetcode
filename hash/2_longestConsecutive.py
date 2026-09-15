"""
最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列
（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""

class Solution(object):
    def method(self, nums):
        seen = set(nums)
        cur_count = 0
        cur_num = None
        max_count = 0

        for num in seen:
            if num - 1 not in seen:
                # 注意这个条件，如果没有这个条件会报错（时间超限）
                # 这个条件的含义：只从连续序列的起点开始数
                cur_num = num
                cur_count = 1

                while cur_num + 1 in seen:
                    cur_count +=1
                    cur_num +=1
                max_count = max(cur_count ,max_count)

        return max_count

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
