from typing import List, Optional


# Definition for a binary tree node (由 LeetCode 提供).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result
