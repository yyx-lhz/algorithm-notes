# Day 06 · 2026-08-04

**题目**: [LeetCode 153. 寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/)

**标签**: 数组 / 二分查找 / 旋转数组 / Python3

---

## 思路

这道题给的是一个原本升序、但在某个点旋转过的数组，要求找到最小值，时间复杂度 O(log n)。

旋转后的数组有一个关键性质：**以最小值为界，左边一段递增，右边一段递增，且左边的最小值比右边的最大值还要大**。

二分的时候，每次取中间点 `mid`，跟**最右边的值** `nums[right]` 比较，分两种情况：

### 情况一：`nums[mid] < nums[right]`

```
        mid          right
         │             │
   [4, 5, 0, 1, 2, 3]
         └─────┘
         这一段递增
```

`mid` 到 `right` 是递增的，说明这一段没有"断崖"，最小值一定在 `mid` **左边（包括 mid 自己）**。

→ `right = mid`（mid 自己可能就是最小值，不能跳过）

### 情况二：`nums[mid] > nums[right]`

```
   left       mid          right
    │          │             │
   [4, 5, 6, 7, 0, 1, 2]
             └──────────┘
              这里有断崖
```

`mid` 比 `right` 大，说明旋转的"断崖"就在 `mid` 到 `right` 之间，最小值一定在 `mid` **右边**。

→ `left = mid + 1`（mid 自己肯定不是最小值，可以跳过）

### 为什么只和最右边比？

- 跟最左边比无法判断"断崖"在哪一侧
- `nums[mid] < nums[right]` → 右侧有序 → 最小值在左侧
- `nums[mid] > nums[right]` → 断崖在右侧 → 最小值在右侧

每次砍掉一半，二分到底，`left` 和 `right` 重合的位置就是最小值。

---

## 解题过程

1. 初始化 `left = 0`, `right = len(nums) - 1`。
2. `while left < right`:
   - 取 `mid = (left + right) // 2`
   - 如果 `nums[mid] < nums[right]`，说明右侧有序，最小值在左侧（含 mid）：`right = mid`
   - 否则 `nums[mid] > nums[right]`，断崖在右侧，最小值在 mid 右边：`left = mid + 1`
3. 退出循环时 `left == right`，返回 `nums[left]` 就是最小值。

**关键点**：`nums[mid] < nums[right]` 时 `right = mid` 而不是 `right = mid - 1`——因为 mid 自己可能就是最小值，不能跳过。这是这道题跟常规二分的最大区别。

---

## 复杂度

- 时间复杂度: **O(log n)** —— 每次砍掉一半
- 空间复杂度: **O(1)** —— 只使用常数个变量

---

## 代码

见 [`153-find-minimum-in-rotated-sorted-array.py`](./153-find-minimum-in-rotated-sorted-array.py)

---

## 易错点

1. 边界更新写错。

   - `nums[mid] < nums[right]` → `right = mid`（不是 `mid - 1`！mid 可能就是最小值）
   - `nums[mid] > nums[right]` → `left = mid + 1`（mid 肯定不是最小值，可以跳过）

2. 循环条件用 `left <= right` 导致死循环。

   这道题要用 `left < right`，因为 `left == right` 时已经定位到最小值。

3. 跟 LeetCode 33（搜索目标值）搞混。

   33 是找具体 target，153 是找最小值——不需要额外的 target 参数，只要一直往"断崖方向"收缩。

---

## 示例

```text
nums = [4, 5, 6, 7, 0, 1, 2]

初始: left=0, right=6, mid=3
  nums[mid]=7 > nums[right]=2 → 断崖在右侧 → left = 4

left=4, right=6, mid=5
  nums[mid]=1 < nums[right]=2 → 右侧有序 → right = 5

left=4, right=5, mid=4
  nums[mid]=0 < nums[right]=1 → 右侧有序 → right = 4

left=4, right=4 → 退出 → 返回 nums[4] = 0 ✅
```

```text
nums = [1, 2, 3, 4, 5]（未旋转）

nums[mid]=3 < nums[right]=5 → right = 2
nums[mid]=2 < nums[right]=3 → right = 1
nums[mid]=1 < nums[right]=2 → right = 0
退出 → 返回 nums[0] = 1 ✅
```

---

## 关联题目

- LeetCode 154 — 含有重复元素的版本
- LeetCode 33 — 搜索旋转排序数组
- LeetCode 81 — 搜索旋转排序数组 II
