# Day 09 · 2026-08-16

**题目**: [LeetCode 141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/)

**标签**: 链表 / 快慢指针 / 龟兔赛跑 / Python3

---

## 思路

这道题的核心是判断链表里有没有环。最经典的解法是**快慢指针**，也叫龟兔赛跑（Floyd's Cycle Detection）。

### 基本思想

设置两个指针，让它们在同一条线上跑：

- `slow`（慢指针）：每次走 1 步
- `fast`（快指针）：每次走 2 步

分两种情况：

**没有环**：`fast` 会先跑到链表末尾（None），永远追不上 `slow`，两个指针不会再相遇。

**有环**：两个指针最终都会进入环里绕圈。`fast` 比 `slow` 快，每绕一圈就追近 1 步，最终一定会"追上" `slow`——两个指针指向同一个节点。

所以判断标准就一句话：**快指针能不能追上慢指针。追得上就有环，追不上就没环。**

### 生活化比喻

操场跑圈。两个人从同一起点出发，一个人走路（每次 1 步），一个人跑步（每次 2 步）。

- 如果是**直线跑道**（无环链表）：跑步的人冲到终点（None）就结束了，两人不会再见面。
- 如果是**环形跑道**（有环链表）：跑步的人速度快，绕一圈之后会从后面追上走路的人——两人在跑道上再次相遇。

相遇的那一刻，就证明跑道是环形的。

### 为什么 fast 每次走 2 步，而不是 3 步或更多

走 2 步保证"每轮循环 fast 和 slow 的距离缩小 1"。只要相对速度是 1，fast 就一定会一步一步追近，不会"跳过" slow。走 3 步可能在某些环长度下永远错过。

---

## 解题过程

1. 初始化 `slow = head`, `fast = head`。
2. `while fast and fast.next:` 循环：
   - `slow = slow.next` — 慢指针走 1 步
   - `fast = fast.next.next` — 快指针走 2 步
   - 如果 `slow == fast` — 追上了，说明有环，返回 True
3. 循环结束（fast 跑到 None）— 说明链表有尽头，无环，返回 False。

**关键点**：循环条件是 `fast and fast.next`。因为 fast 每次走 2 步，必须保证 `fast.next` 存在，否则 `fast.next.next` 会报 NoneType 错误。

---

## 复杂度

- 时间复杂度: **O(n)** —— 无环时 fast 走 n/2 步到结尾；有环时 slow 最坏绕环一圈被追上
- 空间复杂度: **O(1)** —— 只使用两个指针，不需要哈希表存已访问节点

---

## 代码

见 [`141-linked-list-cycle.py`](./141-linked-list-cycle.py)

---

## 易错点

1. 循环条件只写 `while fast:` 忘记 `fast.next`。

   fast 走 2 步需要 `fast.next` 存在，否则 `fast.next.next` 对 None 取 next 会报错。

2. 把 `slow == fast` 的判断放在初始化时。

   两个指针初始都是 head，必须先走再比较。正确顺序：先移动，再判断。

3. 无环链表只有 1 个节点时。

   `head.next` 为 None → `fast.next` 为 None → 循环直接跳过 → 返回 False，正确。

---

## 示例

```text
有环: 3 → 2 → 0 → -4
           ↑__________↓

初始: slow=3, fast=3

第 1 轮:
  slow = 2
  fast = 0
  slow != fast

第 2 轮:
  slow = 0
  fast = 2
  slow != fast

第 3 轮:
  slow = -4
  fast = -4
  slow == fast → 追上！返回 True ✅
```

```text
无环: 1 → 2 → 3 → None

初始: slow=1, fast=1

第 1 轮: slow=2, fast=3
第 2 轮: slow=3, fast=None → fast.next 为 None → 循环结束
返回 False ✅
```

---

## 关联题目

- LeetCode 142 — 环形链表 II（找到环的入口）
- LeetCode 876 — 链表的中间节点（快慢指针变形）
- LeetCode 234 — 回文链表
