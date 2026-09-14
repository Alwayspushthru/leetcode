"""
1.两数之和
给定一个整数数组nums和一个整数目标值 target,请你在该数组中找出和为目标值target的那两个整数,
并返回它们的数组下标。你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
"""
import sys

class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i, num in enumerate(nums):
            need = target-num
            if need in seen:
                return [i,seen[need]]
            seen[num] = i
        return []

def main():
    data = list(map(int, input().split()))
    if not data:
        return 

    target = data[-1]
    nums = data[0:-1]
    print(Solution().twoSum(nums,target))

if __name__ == "__main__":
    main()
