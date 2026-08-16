# Day 11 · 2026-08-16

**题目**: [LeetCode 19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

**标签**: 链表 / 双指针 / 快慢指针 / Python3

---

## 思路

这道题的核心难点：链表的倒数第 N 个节点**没办法直接从前往后数**——因为你不知道链表有多长，也就不知道倒数第 N 个在哪。

### 基本思想：双指针保持固定距离

设置两个指针，让它们**始终相距 N 个节点**，然后一起向前移动：

1. `fast` 指针**先走 N 步**
2. 然后 `slow` 和 `fast` **同时走**，每次各走 1 步
3. 当 `fast` 走到链表末尾（None）时，`slow` 正好指向**倒数第 N 个节点**

为什么成立：`fast` 在末尾，`slow` 在它后面 N 个位置——从后往前数，`slow` 就是倒数第 N 个。

### 为什么需要哑节点（dummy node）

要**删除**倒数第 N 个节点，光找到它还不够——需要知道它的**前一个节点**，才能让前一个节点跳过它。

所以让 `slow` 从 dummy（head 前面的虚拟节点）出发。当 `fast` 到末尾时，`slow` 正好停在**倒数第 N 个节点的前一个**，直接：

```python
slow.next = slow.next.next   # 跳过目标节点，完成删除
```

**dummy 的另一个作用**：如果要删的就是头节点（N = 链表长度），没有 dummy 就没有"头的前一个节点"，无法删除。有 dummy 后统一处理，不需要特判。

### 生活化比喻

一列队伍，要从队尾往前数第 3 个人——但你只能从队头开始数，不知道队伍有多长。

办法：找两个人。A 先往前走 3 步。然后 A、B 一起按同样速度往前走。等 A 走到队伍尽头时，B 站的位置正好就是"倒数第 3 个"。这就是"保持距离"的核心——**A 和 B 之间的距离永远不变，A 到头的瞬间，B 的位置就由这段距离决定了。**

要"踢出"B 站着的那个人，就让 B 站在他前面一个人的位置——这样 B 一伸手就能把他拉出队伍。B 的起点从 dummy 开始，就是这个目的。

---

## 解题过程

1. 创建哑节点 `dummy`，`dummy.next = head`。
2. `slow = dummy`, `fast = head`。
3. `fast` 先走 N 步。
4. `while fast:` → `slow` 和 `fast` 各走 1 步，直到 `fast` 到 None。
5. 此时 `slow` 在目标节点的前一个 → `slow.next = slow.next.next` 删除。
6. 返回 `dummy.next`（新链表头）。

**关键点**：返回的是 `dummy.next` 而不是 `head`——因为 head 可能已经被删掉了。

---

## 复杂度

- 时间复杂度: **O(n)** —— fast 先走 N 步，再和 slow 一起走完剩余部分，总共一遍遍历
- 空间复杂度: **O(1)** —— 只使用两个指针和一个哑节点

---

## 代码

见 [`19-remove-nth-node-from-end-of-list.py`](./19-remove-nth-node-from-end-of-list.py)

---

## 易错点

1. 不用 dummy，直接从头找。

   删除头节点的场景无法处理，需要额外特判。

2. `fast` 先走 N 步 vs N-1 步分不清。

   本题 `fast = head` 先走 N 步，`slow = dummy`。这样 fast 到 None 时，slow 正好停在目标的前一个。若两个指针起点不同，走的步数也要相应调整。

3. 返回 `head` 而不是 `dummy.next`。

   当删除头节点时，head 已经是无效节点了。

4. `fast` 走 N 步时 `fast.next` 越界。

   题目保证 N 不超过链表长度，`while n > 0` 直接走即可，但边界判断要留意空链表。

---

## 示例

```text
链表: 1 → 2 → 3 → 4 → 5
N = 2（删除倒数第 2 个，即节点 4）

dummy → 1 → 2 → 3 → 4 → 5
slow = dummy, fast = head

fast 先走 2 步: fast = 3

一起走:
  第1轮: slow=1, fast=4
  第2轮: slow=2, fast=5
  第3轮: slow=3, fast=None → 停止

slow 指向 3（目标节点 4 的前一个）

slow.next = slow.next.next  → 3 直接连 5

结果: 1 → 2 → 3 → 5 ✅
```

```text
链表: 1
N = 1（删除头节点）

dummy → 1
fast 先走 1 步: fast = None

while fast: 不进入循环 → slow 停在 dummy

slow.next = slow.next.next → dummy.next = None

返回 dummy.next = None ✅（空链表）
```

---

## 关联题目

- LeetCode 876 — 链表的中间节点（双指针）
- LeetCode 141/142 — 环形链表（快慢指针）
- LeetCode 21 — 合并两个有序链表
