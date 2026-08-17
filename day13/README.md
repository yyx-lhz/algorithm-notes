# Day 13 · 2026-08-17

**题目**: [LeetCode 101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/)

**标签**: 二叉树 / 递归 / 双指针 / Python3

---

## 思路

对称二叉树的定义：根节点左右两侧**互为镜像**——左子树的左边对应右子树的右边，左子树的右边对应右子树的左边。

### 核心转化

不要检查"一棵树本身对不对称"，而是检查**两棵树是否互为镜像**：

```
isMirror(左子树, 右子树)
```

两个节点互为镜像，需要同时满足：

1. 两个节点的值相等
2. 左节点的左孩子 == 右节点的右孩子（镜像对应）
3. 左节点的右孩子 == 右节点的左孩子（交叉对应）

### 递归结构

```python
def isMirror(p, q):
    if not p and not q: return True          # 都为空 → 对称
    if not p or not q:  return False         # 一个空一个不空 → 不对称
    if p.val != q.val:  return False         # 值不等 → 不对称
    # 交叉比较：p 的左 vs q 的右，p 的右 vs q 的左
    return isMirror(p.left, q.right) and isMirror(p.right, q.left)
```

### 生活化比喻

照镜子。你举起左手，镜子里的人举起的是"他的右手"。对称树检查的就是这种**交叉对应**——左边的左边必须等于右边的右边，而不是左边的左边等于右边的左边。

---

## 解题过程

1. 空树 → 对称，返回 True。
2. 调用 `isMirror(root.left, root.right)`：
   - 都为空 → True
   - 只有一个为空 → False
   - 值不相等 → False
   - 递归检查：`(p.left, q.right)` 和 `(p.right, q.left)` 都对称才返回 True
3. 返回递归结果。

**关键点**：递归的对应关系是**交叉的**——左左对右右、左右对右左。写成同侧就错了。

---

## 复杂度

- 时间复杂度: **O(n)** —— 每个节点访问一次
- 空间复杂度: **O(h)** —— 递归栈深度为树高，最坏 O(n)（链状树），平均 O(log n)

---

## 代码

见 [`101-symmetric-tree.py`](./101-symmetric-tree.py)

---

## 易错点

1. 把对应关系写成同侧。

   错误：`isMirror(p.left, q.left)`。正确：`isMirror(p.left, q.right)`——镜像必须交叉。

2. 空节点判断顺序不对。

   必须先判 `都为空`，再判 `一个为空`。顺序反了会出错。

3. 只比较根节点的左右孩子，忘记递归深层。

   对称是**整棵树**的对称，每一层都要交叉比较。

---

## 示例

```text
       1
     /   \
    2     2
   / \   / \
  3   4 4   3
  ↑ 左右交叉对应 ↑

isMirror(2, 2): 值相等
  isMirror(3, 3): 值相等，都是叶子 → True
  isMirror(4, 4): 值相等，都是叶子 → True
  → True ✅
```

```text
       1
     /   \
    2     2
     \     \
      3     3

isMirror(2, 2): 值相等
  isMirror(2.left=None, 2.right=3): 一个空一个不空 → False
  → 不对称 ❌
```

---

## 关联题目

- LeetCode 100 — 相同的树
- LeetCode 226 — 翻转二叉树
- LeetCode 572 — 另一棵树的子树
