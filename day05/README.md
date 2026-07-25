# Day 05 · 2026-07-26

**题目**: [LeetCode 34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

**标签**: 数组 / 二分查找 / 边界查找 / Python3

---

## 思路

这道题要求在有序数组里找到 `target` 的最左位置和最右位置,并且要求时间复杂度是 `O(log n)`。

因为数组已经排好序,所以不能用从左到右扫描的方式,应该用二分查找。

普通二分只能找到某一个 `target`,但题目要的是一段区间:

- 最左边的 `target`
- 最右边的 `target`

所以可以拆成两个二分:

1. `find_left()` 找左边界
2. `find_right()` 找右边界

找左边界时,如果 `nums[mid] == target`,不能直接返回,而是先记录答案,然后继续往左找:

```python
answer = mid
right = mid - 1
```

找右边界时,如果 `nums[mid] == target`,同样不能直接返回,而是先记录答案,然后继续往右找:

```python
answer = mid
left = mid + 1
```

如果最后没有找到目标值,`answer` 会保持 `-1`,正好符合题目要求。

---

## 解题过程

1. 写一个 `find_left()`:
   - 初始化 `left = 0`,`right = len(nums) - 1`,`answer = -1`。
   - 如果 `nums[mid] > target`,说明目标在左边,移动 `right`。
   - 如果 `nums[mid] < target`,说明目标在右边,移动 `left`。
   - 如果 `nums[mid] == target`,记录 `mid`,然后继续向左收缩。
2. 写一个 `find_right()`:
   - 整体逻辑和 `find_left()` 类似。
   - 区别是命中目标后继续向右收缩。
3. 返回 `[find_left(), find_right()]`。

**关键点**:找到 `target` 后不要马上返回。边界题的核心就是“命中之后继续压缩搜索区间”。

---

## 复杂度

- 时间复杂度: **O(log n)** —— 两次二分查找,仍然是对数级别
- 空间复杂度: **O(1)** —— 只使用常数个变量

---

## 代码

见 [`34-find-first-and-last-position-of-element-in-sorted-array.py`](./34-find-first-and-last-position-of-element-in-sorted-array.py)

---

## 易错点

1. 命中 `target` 后直接返回。

   这样只能得到某一个位置,不能保证是最左或最右。

2. 左边界和右边界的收缩方向写反。

   - 左边界:命中后 `right = mid - 1`
   - 右边界:命中后 `left = mid + 1`

3. 忘记处理不存在的情况。

   用 `answer = -1` 作为默认值,没有找到时自然返回 `-1`。

---

## 示例

```text
nums = [5, 7, 7, 8, 8, 10]
target = 8

返回: [3, 4]
```

解释:

```text
8 第一次出现在下标 3
8 最后一次出现在下标 4
```
