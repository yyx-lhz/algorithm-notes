# Day 08 · 2026-08-14

**题目**: [LeetCode 206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)

**标签**: 链表 / 迭代 / 双指针 / Python3

---

## 思路

这道题的核心是区分两个概念：**换标签**和**换数据结构**。

- **换标签**：节点还是那些节点，只是把每个节点的 `next` 指针重新指向
- **换数据结构**：把链表整体翻转，每个箭头反向

反转链表不是把节点挪来挪去，而是**把每个节点的箭头反向**。

原来的链表：

```text
1 → 2 → 3 → 4 → 5 → None
```

反转后：

```text
None ← 1 ← 2 ← 3 ← 4 ← 5
```

### 三指针迭代法

维护三个变量：

| 指针 | 含义 |
|------|------|
| `pre` | 已经反转好的部分的头 |
| `current` | 当前正在处理的节点 |
| `next` | 临时保存的、下一个要处理的节点 |

每一步做三件事：

1. **先把 `current.next` 存下来**——不存的话，改了指向就找不回下一个节点了
2. **把 `current.next` 指向 `pre`**——箭头反向，让 `2` 打到 `1` 上
3. **`pre` 和 `current` 各往前挪一步**——`pre = current`，`current = next`

### 为什么必须先存 next

```python
next = current.next    # 先保存下一个节点
current.next = pre     # 现在可以安全地改指向了
```

如果不先保存，`current.next = pre` 之后，原来的下一个节点就丢了——链断了，后面全找不回来。

### 生活化比喻

一列人手拉手排成一队，每个人拉着前面的人。反转就是让每个人转身去拉后面的人。但转身之前得先看清楚"我原来拉的是谁"，不然转完身就不知道队伍在哪了。`next = current.next` 就是"先看清原来拉的是谁"。

---

## 解题过程

1. 初始化 `pre = None`（原链表头前面是空），`current = head`。
2. `while current:` 循环处理每个节点：
   - `next = current.next` — 保存下一个节点
   - `current.next = pre` — 当前节点反向指向
   - `pre = current` — pre 前移
   - `current = next` — current 前移
3. 循环结束，`current` 为 None，`pre` 就是反转后的新链表头，返回 `pre`。

**关键点**：四行代码的顺序不能乱。先存 next，再改指向，最后两个指针一起前移。

---

## 复杂度

- 时间复杂度: **O(n)** —— 遍历每个节点一次
- 空间复杂度: **O(1)** —— 只使用三个指针，原地反转

---

## 代码

见 [`206-reverse-linked-list.py`](./206-reverse-linked-list.py)

---

## 易错点

1. 忘了先保存 `next`，直接 `current.next = pre`。

   链断了，后面的节点全部丢失。

2. 指针前移顺序写反。

   正确顺序：先 `pre = current`，再 `current = next`。反了的话两个指针指向同一个节点。

3. 返回 `current` 而不是 `pre`。

   循环结束时 `current` 是 None，`pre` 才是新链表头。

4. 空链表没处理。

   `head` 为 None 时，`while current` 直接跳过，返回 `pre = None`，天然正确。

---

## 示例

```text
输入: 1 → 2 → 3 → None

初始: pre=None, current=1

第 1 步:
  next = 2          （先存下 2）
  current.next=None （1 的箭头反向，指向 None）
  pre = 1           （pre 前移）
  current = 2       （current 前移）
  状态: None ← 1    2 → 3

第 2 步:
  next = 3
  current.next = 1  （2 的箭头反向，打到 1 上）
  pre = 2
  current = 3
  状态: None ← 1 ← 2    3

第 3 步:
  next = None
  current.next = 2  （3 的箭头反向，打到 2 上）
  pre = 3
  current = None
  状态: None ← 1 ← 2 ← 3

循环结束，返回 pre = 3 → 2 → 1 → None ✅
```

---

## 关联题目

- LeetCode 92 — 反转链表 II（反转一部分）
- LeetCode 25 — K 个一组反转链表
- LeetCode 234 — 回文链表（快慢指针 + 反转）
