# Day 19 · LeetCode 148. 排序链表（Sort List）

## 解题思路

使用归并排序：**先把链表从中间断成两段，递归排好左右两段，再把两个有序链表合并。**

链表不能像数组一样通过下标快速访问任意位置，但可以沿着 `next` 遍历，也可以通过修改 `next` 重新连接节点，因此适合归并排序。不是说链表只能用这一种排序方式，而是这种方法能在 O(n log n) 时间内完成排序。

### 1. 递归出口

```python
if not head or not head.next:
    return head
```

空链表或只有一个节点的链表已经有序，直接返回它的头节点。

### 2. 用快慢指针找到切分位置

```python
slow = head
fast = head.next

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

- `slow` 每轮走一步，`fast` 每轮走两步；快指针初始比慢指针靠后一个节点。
- 循环结束时，`slow` 是左半段最后一个节点，`slow.next` 是右半段第一个节点。
- 偶数长度时，`slow` 停在两个中间节点中的左边一个；奇数长度时，停在正中间，左半段比右半段多一个节点。

例如：

```text
4 → 2 → 1 → 3        slow 停在 2，拆成 [4, 2] 和 [1, 3]
4 → 2 → 1 → 3 → 5    slow 停在 1，拆成 [4, 2, 1] 和 [3, 5]
```

这里让 `fast = head.next`，能保证两个节点时也拆成一边一个。如果只把它改成 `fast = head` 而保持其余逻辑不变，两节点链表会无法缩小左半段，导致递归不能结束。

条件必须先判断 `fast`，再访问 `fast.next`。Python 的 `and` 从左往右短路求值；写成 `while fast.next and fast` 时，可能在 `fast = None` 时访问 `None.next` 而报错。

### 3. 保存左右入口，再主动断开

```python
left = head
right = slow.next
slow.next = None
```

`slow.next` 不会在找中点后自动变成 `None`，需要主动断开。必须先把右半段入口保存到 `right`，否则断开后就丢失了从这里访问右半段的入口。

这里是让 `left` 指向原来的头节点，让 `right` 指向右半段的头节点；不是写 `head = left` 或 `head = right`，也不是复制出新的节点。

### 4. 递归排序左右两段

```python
left = self.sortList(left)
right = self.sortList(right)
return self.merge(left, right)
```

每次递归都重复“拆分 → 排序左右两段 → 合并”。一直拆到单节点，再随着递归返回逐层合并。

排序后头节点可能变化，所以要用 `left` 和 `right` 接住各自返回的新头节点。调用 `merge` 时，这两段已经分别有序。

## merge 如何合并

### 1. 哨兵节点保留结果入口

```python
dummy = ListNode(0)
cur = dummy
```

`dummy` 是一个辅助节点，值 0 没有排序含义，也不会参与比较。`cur` 最初与它指向同一个节点，之后不断向后移动，指向已合并部分的末尾；`dummy` 一直保留在入口处。

### 2. 比较两个剩余链表的头节点

```python
while left and right:
    if left.val <= right.val:
        cur.next = left
        left = left.next
    else:
        cur.next = right
        right = right.next
    cur = cur.next
```

以右边更小为例：

1. `cur.next = right`：把右边当前节点接到结果末尾。
2. `right = right.next`：右边的待处理指针前进一步。
3. `cur = cur.next`：结果尾指针前进一步，方便下一次接节点。

这里修改的是节点之间的连接，不是把 `cur` 复制到 `right`，也不是把 `right.next` 改成头节点。左边更小时操作对称；相等时先接左边，保持稳定性。

### 3. 一边用完后接上另一边

```python
cur.next = left if left else right
```

循环条件是 `while left and right`，所以退出时至少有一边为空。上面这一行等价于：

```python
if left:
    cur.next = left
else:
    cur.next = right
```

如果 `left` 还指着节点，就接左边；否则接右边。剩余部分本来就有序，而且不小于已合并部分的末尾，因此可以整段接上，不需要再逐个比较。两边都为空时，接上的就是 `None`。

### 4. 为什么返回 dummy.next

```text
dummy → 1 → 2 → 3 → 4 → None
        ↑
    真正的结果头节点
```

`dummy` 本身不属于答案；`dummy.next` 指向排序后第一个真实节点。返回这个头节点，就能沿着 `next` 访问整条结果链表。

因此返回 `dummy.next`，而不是 `dummy` 或已经移动到后面的 `cur`。

## 例子

```text
拆分：
[4, 2, 1, 3]
       ↓
[4, 2]   [1, 3]
   ↓        ↓
[4] [2]  [1] [3]

逐层合并：
[4] + [2] → [2, 4]
[1] + [3] → [1, 3]
[2, 4] + [1, 3] → [1, 2, 3, 4]
```

最后一次合并依次接上 1、2、3，右半段用完，再把左半段剩下的 4 接上。

## Python 3 代码

完整代码：[148-sort-list.py](./148-sort-list.py)。`ListNode` 由 LeetCode 提供；在本地运行时，需要先定义注释中的节点类。

```python
from typing import Optional

# Definition for singly-linked list (由 LeetCode 提供).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if not head or not head.next:
            return head

        # slow 停在左半段的最后一个节点。
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next
        slow.next = None  # 先保存右半段入口，再断开链表。

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        cur = dummy

        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        # 至少一边已经为空，直接接上另一边的剩余链表。
        cur.next = left if left else right
        return dummy.next
```

## 易错点

- 快指针每轮走两步，慢指针走一步；“快一步”容易与初始位置混淆。
- `slow` 是左半段末尾，不能笼统说成永远在“中心点左边一个”。
- 先保存 `right = slow.next`，再执行 `slow.next = None`。
- 先判断 `fast` 是否存在，再访问它的 `next`。
- 接节点用 `cur.next = left/right`；移动待处理指针用 `left = left.next` 或 `right = right.next`。
- 每次选完一个节点都要移动 `cur`；最后返回 `dummy.next`。

## 边界与复杂度

- 空链表、单节点直接返回；两个节点可以正常拆分和合并。
- 奇偶长度、重复值、负数、已经有序或逆序的链表都适用。
- 时间：O(n log n)。递归有 O(log n) 层，每层拆分和合并的总工作量为 O(n)。
- 额外空间：O(log n)，来自递归调用栈；单次迭代合并只用 O(1) 辅助空间。
- 本笔记是自顶向下的递归版本，不满足进阶要求中的 O(1) 额外空间；若要做到 O(1)，可使用自底向上的迭代归并排序。
