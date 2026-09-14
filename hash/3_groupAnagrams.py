"""
给你一个字符串数组，请你将字母异位词组合在一起。
可以按任意顺序返回结果列表。

字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
解释：
在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。

"""
class Solution(object):
    def method(self, strs):
        hashmap = {}
        for s in strs:
            key = ''.join(sorted(s))
            # sorted 得到字符列表 
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
        return list(hashmap.values())

def main():
    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        strs = line.split()
        print(Solution().method(strs))

if __name__ == "__main__":
    main()