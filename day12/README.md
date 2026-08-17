# Day 12 · 2026-08-17

**题目**: [LeetCode 199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/)

**标签**: 二叉树 / 层序遍历 / BFS / Python3

---

## 思路

右视图 = 站在树的右边看过去，每一层能看到的**最右边的那个节点**。

关键转化：**层序遍历（BFS），每一层只取最后一个节点**。

### 为什么是层序遍历

右视图要求"每层一个节点"。层序遍历天然按层处理——队列里一层一层弹出。每一层遍历完后，这一层**最后访问的节点**就是最右边的节点。

### BFS 队列怎么按层走

```python
queue = [root]
while queue:
    size = len(queue)          # 当前层的节点个数
    for i in range(size):
        node = queue.pop(0)    # 弹出本层一个节点
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    # 这层处理完
```

`size = len(queue)` 先记录本层个数，再用 `for i in range(size)` 精确控制"只处理这一层"——处理完时，队列里恰好全是下一层的节点。

**每层最后弹出的节点**（`i == size - 1` 那个）就是右视图看到的节点。

### 生活化比喻

一栋楼的电梯每一层停一次。你站在楼的右侧看，每一层只看到**最靠右的那扇窗户**。层序遍历就是坐电梯一层层看，每层扫一眼，记住最右那扇窗户。

---

## 解题过程

1. 空树 → 返回空列表。
2. 初始化 `queue = [root]`，`result = []`。
3. `while queue:` 循环每层：
   - `size = len(queue)` 记录本层大小
   - `for i in range(size)`：弹出节点，左孩子右孩子依次入队
   - 当 `i == size - 1`（本层最后一个）→ 加入 result
4. 返回 `result`。

**关键点**：`size` 必须在 for 循环前取。如果在循环内动态取 `len(queue)`，会把下一层的节点也混进来，层就分不清了。

---

## 复杂度

- 时间复杂度: **O(n)** —— 每个节点访问一次
- 空间复杂度: **O(n)** —— 队列最多容纳一整层的节点

---

## 代码

见 [`199-binary-tree-right-side-view.py`](./199-binary-tree-right-side-view.py)

---

## 易错点

1. 在 for 循环里用 `len(queue)` 做边界。

   队列在循环中被不断 append，`len(queue)` 一直变。必须先 `size = len(queue)` 固定本层大小。

2. 右孩子和左孩子入队顺序写反。

   层序遍历入队顺序无所谓（反正每层都要扫完），但要保证弹出的顺序一致。

3. 取"本层第一个"而不是"本层最后一个"。

   右视图要的是**最右**，也就是本层最后弹出的节点。

---

## 示例

```text
       1
     /   \
    2     3
     \     \
      5     4

层序遍历:
  第 1 层: [1]           → 最后节点 1
  第 2 层: [2, 3]        → 最后节点 3
  第 3 层: [5, 4]        → 最后节点 4

右视图: [1, 3, 4] ✅
```

---

## 关联题目

- LeetCode 102 — 二叉树的层序遍历
- LeetCode 107 — 二叉树的层序遍历 II
- LeetCode 637 — 二叉树的层平均值
