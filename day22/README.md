# Day 22 · LeetCode 35. 搜索插入位置

**题目**: [LeetCode 35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/)

**标签**: 数组 / 二分查找 / Python3

---

## 我的思路

这题就是经典的二分查找。数组已经按升序排列，而且没有重复元素。如果一个个比较，最坏要检查整个数组，时间复杂度是 **O(n)**；如果使用二分查找，每次排除大约一半的搜索范围，时间复杂度是 **O(log n)**。题目要求 O(log n)，所以使用二分查找。

找到目标值就返回它的下标；如果没有找到，就返回它应该插入的位置，让插入后的数组仍然有序。这里只计算位置，不需要真的往数组里插入元素。

## left、right、mid 分别是什么？

它们都是数组的**下标**，不是数组里的数值。

- `left`：当前搜索范围的左端点，初始为 `0`。
- `right`：当前搜索范围的右端点，初始为 `len(nums) - 1`。
- `mid = (left + right) // 2`：当前范围中间的下标，`//` 表示整除。
- `nums[mid]`：中间位置的数值，用来和 `target` 比较。

本解法使用闭区间 `[left, right]`，两个端点都包含在搜索范围内。

每轮比较后：

1. `target == nums[mid]`：找到了，直接 `return mid`。
2. `target > nums[mid]`：中间值及其左侧都太小，令 `left = mid + 1`。
3. `target < nums[mid]`：中间值及其右侧都太大，令 `right = mid - 1`。

`mid` 已经检查过了，因此下一轮用 `mid + 1` 或 `mid - 1` 排除它，保证范围持续缩小。

## 为什么是 while left <= right？

这里容易把两种“等于”混在一起：

| 判断 | 比较的对象 | 含义 |
|------|------------|------|
| `left <= right` | 两个下标 | 搜索范围里是否还有位置需要检查 |
| `target == nums[mid]` | 目标值与中间值 | 当前检查的数是不是目标值 |

`left == right` 只表示**还剩一个位置**，不表示那个位置的数等于目标值。所以它与循环内部的相等判断并不重复。

例如 `nums = [1]`、`target = 1`，初始 `left = right = 0`。如果本解法只把条件改成 `left < right`，就不会进入循环检查这个唯一的元素；改成 `target = 2` 时，更会直接返回错误的位置 `0`，而正确插入位置是 `1`。

使用 `left <= right` 才会检查最后一个位置。只有 `left > right` 时，闭区间才是空的，搜索才结束。其他二分写法可以使用 `<`，但必须配套不同的区间定义或结束处理，不能只改这一处。

## 没找到时，为什么 return left？

每轮缩小范围时，都保持两个事实：

- `left` 左边的所有元素都小于 `target`。
- `right` 右边的所有元素都大于 `target`。

因为数组有序，如果 `nums[mid] < target`，就能把截至 `mid` 的这一段全部排除；反之，如果 `nums[mid] > target`，就能把从 `mid` 开始的这一段全部排除。

如果一直没有找到相等的元素，循环结束时两个端点刚好交错：`left == right + 1`。此时 `left` 左边的数都比目标小，从 `left` 开始的数都比目标大，因此 **`left` 正好就是保持有序的插入位置**。

以 `nums = [1, 3, 5, 6]`、`target = 2` 为例：

| 轮次 | left | right | mid | nums[mid] | 操作 |
|------|------|-------|-----|-----------|------|
| 1 | 0 | 3 | 1 | 3 | 2 < 3，令 right = 0 |
| 2 | 0 | 0 | 0 | 1 | 2 > 1，令 left = 1 |
| 结束 | 1 | 0 | — | — | left > right，返回 1 |

```text
原数组：[1,    3, 5, 6]
插入后：[1, 2, 3, 5, 6]
           ↑
        插入下标 1
```

这个结论也包含两端：目标比所有数都小时，返回 `0`；目标比所有数都大时，返回 `len(nums)`，表示插在末尾。返回这个位置不需要访问 `nums[left]`，所以 `left == len(nums)` 是合法的。

## Python 3 代码

完整代码：[35-search-insert-position.py](./35-search-insert-position.py)。

```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

## 复杂度

设 `n = len(nums)`。

- 时间复杂度：**O(log n)**，每轮把搜索范围缩小约一半。
- 辅助空间复杂度：**O(1)**，只使用 `left`、`right`、`mid` 等固定数量的变量。
- 对比：逐个比较的线性扫描最坏是 **O(n)**，不能把它也说成 O(log n)。

## 易错点与这次的报错

- 下标 `mid` 和数值 `nums[mid]` 要分清：比较用数值，返回用下标。
- 闭区间只剩一个位置时仍要检查，因此这里使用 `while left <= right`。
- 找到了就在循环内 `return mid`；没找到才在循环结束后 `return left`，不能提前在第一轮就返回。
- `IndentationError: unindent does not match any outer indentation level` 是缩进层级不一致造成的，可能是空格数量不对或混用了 Tab 和空格。
- 统一每层使用 4 个空格。这里的 `return left` 与 `while`、`left = 0` 对齐，位于方法内部、循环外部；在包含 `class Solution` 的完整代码中，这几行前面都是 **8 个空格**。

## 示例自查

| nums | target | 返回位置 | 场景 |
|------|--------|----------|------|
| `[1, 3, 5, 6]` | 5 | 2 | 找到已有元素 |
| `[1, 3, 5, 6]` | 2 | 1 | 插在中间 |
| `[1, 3, 5, 6]` | 7 | 4 | 插在末尾 |
| `[1, 3, 5, 6]` | 0 | 0 | 插在开头 |
| `[1]` | 1 | 0 | 唯一元素就是目标 |
| `[1]` | 2 | 1 | 唯一元素小于目标 |
