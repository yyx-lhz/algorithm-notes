# Day 20 · LeetCode 94. 二叉树的中序遍历

**题目**: [LeetCode 94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

**标签**: 二叉树 / 递归 / DFS / 中序遍历 / Python3

---

## 思路

使用递归进行中序遍历，顺序是：

```text
左子树 → 当前节点 → 右子树
```

对应代码中的三步：

```python
dfs(node.left)
result.append(node.val)
dfs(node.right)
```

`dfs(node.left)` 表示先把整棵左子树按中序遍历处理完；回来后把当前节点的值加入结果列表；最后再遍历整棵右子树。

## 递归出口

```python
if node is None:
    return
```

当 `node is None` 时，说明这条路径已经走到底，当前这层递归直接结束。

这里的 `return` 只负责结束当前的 `dfs` 调用，不是返回最终结果。最终结果由外层函数通过 `return result` 返回。

## Python 3 代码

完整代码：[94-binary-tree-inorder-traversal.py](./94-binary-tree-inorder-traversal.py)。

```python
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
```

## 复杂度

- 时间复杂度：**O(n)**，每个节点访问一次。
- 空间复杂度：**O(h)**，递归调用栈的深度取决于树高 `h`；最坏为 O(n)。

## 易错点

- 中序遍历的顺序是“左 → 根 → 右”。
- 遇到空节点要立即返回，否则继续访问 `node.left` 等属性会报错。
- `dfs(node.left)` 是遍历整棵左子树，不只是访问左孩子。
- `dfs` 中的 `return` 用来结束当前递归；外层的 `return result` 才返回答案。
