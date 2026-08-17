# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q) -> bool:
        # 都为空 → 对称
        if not p and not q:
            return True
        # 一个为空 → 不对称
        if not p or not q:
            return False
        # 值不相等 → 不对称
        if p.val != q.val:
            return False

        # 交叉比较：左左对右右，左右对右左
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
