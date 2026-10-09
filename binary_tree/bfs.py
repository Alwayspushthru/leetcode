import sys
from collections import deque

# 定义二叉树类
class TreeNode:
    def __init__(self, val = 0 , left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(tree_arr):
    # 空树
    if not tree_arr or tree_arr[0] is None:
        return None
    q = []
    rt = TreeNode(tree_arr[0])
    q.append(rt)

    index = 1
    while q and index<len(tree_arr):
        node = q.pop(0)
        # 左孩子
        if index<len(tree_arr) and tree_arr[index] is not None:
            node.left = TreeNode(tree_arr[index])
            q.append(node.left)
        index += 1

        # right
        if index<len(tree_arr) and tree_arr[index] is not None:
            node.right = TreeNode(tree_arr[index])
            q.append(node.right)
        index +=1
    return rt

class Solution(object):
    def bfs(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []

        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)
        return ans

def main():
    tree_str = sys.stdin.read().strip()
    if not tree_str:
        return []
    raw_arr = tree_str.split()
    tree_arr = []
    for raw in raw_arr:
        if raw == "null":
            tree_arr.append(None)
        else:
            tree_arr.append(int(raw))
        # tree_arr -> [1,None,2]数组
    rt = build_tree(tree_arr)
    rt_bfs = Solution().bfs(rt)

    print(rt_bfs)

if __name__ == "__main__":
    main()