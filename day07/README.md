# Day 07 · 2026-08-12

**题目**: [LeetCode 33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)

**标签**: 数组 / 二分查找 / 旋转数组 / Python3

---

## 思路

这道题是 LeetCode 153 的升级版——不是找最小值，而是找一个具体的 `target`。但核心思路是一样的：**利用旋转数组"一半有序、一半无序"的性质，逐步锁定目标范围**。

旋转数组的关键性质：

- 取 `mid` 后，**左半段和右半段必有一段是完全有序的**
- 判断 `target` 在不在有序的这一段里
- 在 → 收缩到有序段继续二分
- 不在 → 收缩到另一段继续二分

### 判断哪一段有序

每次取 `mid`，跟 `nums[left]` 比较：

**情况一：`nums[left] <= nums[mid]` → 左半段有序**

```
   left       mid
    │          │
   [4, 5, 6, 7, 0, 1, 2]
    └───────┘
    这一段递增
```

如果 `nums[left] <= target < nums[mid]` → target 在左半段 → `right = mid - 1`

否则 → target 在右半段 → `left = mid + 1`

**情况二：`nums[left] > nums[mid]` → 右半段有序**

```
   left       mid
    │          │
   [7, 0, 1, 2, 4, 5, 6]
             └──────────┘
             这一段递增
```

如果 `nums[mid] < target <= nums[right]` → target 在右半段 → `left = mid + 1`

否则 → target 在左半段 → `right = mid - 1`

### 跟 LeetCode 153 的关系

153 只找"最小值在哪"，每次只和最右边比。33 多了一个 `target`，所以需要判断 `target` 落在有序段还是无序段。**核心思想是一样的——用"局部有序"来缩小搜索范围。**

---

## 解题过程

1. 初始化 `left = 0`, `right = len(nums) - 1`。
2. `while left <= right`:
   - 取 `mid = (left + right) // 2`
   - 如果 `nums[mid] == target`，直接返回 `mid`
   - 判断左半段是否有序：`nums[left] <= nums[mid]`
     - 左半段有序 → 判断 target 是否在 `[nums[left], nums[mid])` 之间
     - 在 → `right = mid - 1`；不在 → `left = mid + 1`
   - 否则（右半段有序）→ 判断 target 是否在 `(nums[mid], nums[right]]` 之间
     - 在 → `left = mid + 1`；不在 → `right = mid - 1`
3. 没找到 → 返回 `-1`。

**关键点**：`nums[left] <= nums[mid]` 中的 `<=` 不能写成 `<`。`left == mid` 时（只剩两个元素），`nums[left]` 和 `nums[mid]` 是同一个数，仍算"左半段有序"。

---

## 复杂度

- 时间复杂度: **O(log n)** —— 每次砍掉一半
- 空间复杂度: **O(1)** —— 只使用常数个变量

---

## 代码

见 [`33-search-in-rotated-sorted-array.py`](./33-search-in-rotated-sorted-array.py)

---

## 易错点

1. 判断有序段用 `nums[left] <= nums[mid]` 而不是 `<`。

   `left` 和 `mid` 重合时，等号保证逻辑仍走"左半段有序"分支。

2. target 范围比较时边界要带等号。

   - `nums[left] <= target < nums[mid]` → 左半段
   - `nums[mid] < target <= nums[right]` → 右半段

3. 跟 LeetCode 153 搞混更新规则。

   153 不需要判断 target，只需比较 `nums[mid]` 和 `nums[right]`。33 多一个 target，需要额外判断 target 落在哪一段。

---

## 示例

```text
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

初始: left=0, right=6, mid=3 → nums[3]=7
  nums[0]=4 <= 7 → 左半段有序 [4,5,6,7]
  target=0 不在 [4,7) → 在右半段 → left = 4

left=4, right=6, mid=5 → nums[5]=1
  nums[4]=0 <= 1 → 左半段有序 [0,1]
  target=0 在 [0,1) → 在左半段 → right = 4

left=4, right=4, mid=4 → nums[4]=0 == target → 返回 4 ✅
```

```text
nums = [1, 3]
target = 3

left=0, right=1, mid=0 → nums[0]=1
  1 <= 1 → 左半段有序
  target=3 不在 [1,1) → right=0? 不对——
  
  实际：left=0, right=1, mid=0
  nums[0]=1 <= 1 → 左半段有序 [1]
  target=3 > nums[mid]=1 且 target 不在 [1,1) → left = mid + 1 = 1

left=1, right=1, mid=1 → nums[1]=3 == target → 返回 1 ✅
```

---

## 关联题目

- LeetCode 153 — 寻找旋转排序数组中的最小值
- LeetCode 81 — 搜索旋转排序数组 II（含重复元素）
- LeetCode 154 — 寻找旋转排序数组中的最小值 II
