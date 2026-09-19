# Day 21 · LeetCode 46. 全排列

**题目**: [LeetCode 46. 全排列](https://leetcode.cn/problems/permutations/)

**标签**: 数组 / 回溯 / 递归 / Set / Python3

---

## 我的思路

这道题是经典的回溯问题。先把“一条路走到底”弄明白，再理解怎么退回来找其他排列。

用 `path` 记录当前排列，用 `used` 记录当前这条路已经使用过的数字。遍历 `nums`，如果一个数字不在 `used` 里面，就把它放进 `path`，同时加入 `used`，再递归往下放。当 `path` 的长度等于 `nums` 的长度时，一条完整排列就找到了，把它复制到 `result`，然后结束当前这次递归调用。

但答案有好多种，不能找到一条就停止整个算法。所以递归返回以后，要把刚才放进去的数字 `pop()` 出来，同时从 `used` 里面去掉，恢复到选择它之前的状态。接着，当前层的 `for` 循环继续尝试下一个数字，再沿着新的选择往下走。

核心就是：**选择 → 递归 → 撤销选择 → 尝试下一个数字。**

这里的变量叫 `path`（路径）；`pass` 是 Python 关键字，不能用作变量名。题目保证 `nums` 中的数字互不相同，因此可以用数字本身作为 `used` 的元素。

## 找到 [1, 2, 3] 后，到底回到哪里？

以 `nums = [1, 2, 3]` 为例，先沿着这条路往下走：

```text
[] → [1] → [1, 2] → [1, 2, 3]
```

选完 3 以后，还会再调用一次 `backtrack()`。这次调用发现路径已经够长，就保存答案并 `return`。它返回到“选了 3 的那一层”的调用位置，然后从调用后面的语句继续：

```python
backtrack()       # 子调用返回后，从下面继续执行
path.pop()        # 删除 path 最后的 3
used.remove(num)  # 此层 num 仍然是 3，也要从 used 删除
```

恢复后，`path = [1, 2]`，`used = {1, 2}`。注意，`pop()` 只修改 `path`，不会自动修改 `used`，所以两步都要做。

### 3 被移出 used 后，为什么不会马上又选一次 3？

`used` 和 `for` 各管一件事：

- `used` 负责判断：这个数字是否已经在当前路径里，避免同一个排列重复使用一个数字。
- `for` 负责按顺序遍历候选数字：当前层已经处理完 3，就往下一个候选走，不会重新从 1 开始。

在 `nums = [1, 2, 3]` 中，3 已经是最后一个候选，因此这一层的循环结束，函数自然返回上一层（即使末尾没有写 `return`）。每次递归调用都有自己的循环进度和 `num`；子调用不会重置父调用的循环。

接下来发生的是：

```text
保存 [1, 2, 3]
撤销 3：path = [1, 2]，used = {1, 2}
这一层循环已结束，返回选了 2 的那一层
撤销 2：path = [1]，used = {1}
这一层继续遍历，下一个候选是 3
选择 3：path = [1, 3]，used = {1, 3}
进入新的递归调用，新一层从头遍历 nums
跳过 1，选择 2，得到 [1, 3, 2]
```

新调用的循环会从头开始，但返回之后，原来那一层的循环是接着走的。

### 为什么没有直接执行 return result？

终止条件里的 `return` 只结束当前这一次 `backtrack()`。外层 `permute()` 的 `return result`，必须等最初那次 `backtrack()` 把所有分支探索完、真正返回后，才会执行。

## Python 3 代码

完整代码：[46-permutations.py](./46-permutations.py)。

```python
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue

                # 选择：把当前数字加入这条路径。
                path.append(num)
                used.add(num)

                backtrack()

                # 撤销选择：恢复现场，让当前层尝试下一个数字。
                path.pop()
                used.remove(num)

        backtrack()
        return result
```

## 复杂度

设 `n = len(nums)`。

- 时间复杂度：**O(n × n!)**。共有 `n!` 个排列，保存每个排列需要复制 `n` 个元素；各层遍历候选的开销也在这一量级内。
- 辅助空间复杂度：**O(n)**，包括 `path`、`used` 和递归调用栈，不计输出。
- 输出空间复杂度：**O(n × n!)**，用于保存所有排列。

## 易错点

- 找到完整排列后要保存 `path.copy()`，不能直接保存 `path`，否则保存的是同一个不断被修改的列表。
- `path.append(num)` 和 `used.add(num)` 是选择；`path.pop()` 和 `used.remove(num)` 是配套的撤销，两边都要恢复。
- `used` 记录的是当前路径用过的数字，不是整个搜索过程中曾经用过的数字。撤销之后，其他分支仍然可以选它。
- 回溯发生在递归调用返回之后；撤销完成后，当前层循环继续尝试下一个候选。
- 本解法依赖输入数字互不相同；有重复数字的“全排列 II”还需要额外的去重处理。
