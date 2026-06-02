# Day 03 · 2026-06-03

**题目**: [LeetCode 42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/)

**标签**: 数组 / 双指针 / 动态规划 / Python3

---

## 思路

**你选用何种方法解题?**

这道题最朴素的思路是**暴力**:对每个点找它左边的最高和右边的最高,然后两者取较小值减去自己的高度,就是该点能接的水量。但是这样的时间复杂度太高,**会超时**。

所以可以用**双指针**优化。双指针的思想就是**确定一边**:两边里高的那一边可以暂时不管,只看矮的那边。因为水位是由短板决定的 —— 只要矮那一边能"咬住",高的那一边再高也只能填到矮的高度。

所以每次只处理矮的那一侧,用 `left_max` / `right_max` 维护已经走过的最高值,当前点的高度比已走过的最高值低,就能接到 `max - height[i]` 的水。

---

## 解题过程

1. 左右两个指针 `left = 0`、`right = len(height) - 1`,以及 `left_max = 0`、`right_max = 0`、`ans = 0`。
2. 每一步比较 `height[left]` 和 `height[right]`:
   - 如果 `height[left] < height[right]` → 处理左边:
     - 若 `height[left] < left_max`,接水 `ans += left_max - height[left]`
     - 否则更新 `left_max = height[left]`
     - `left += 1`
   - 否则处理右边(对称逻辑):
     - 若 `height[right] < right_max`,接水 `ans += right_max - height[right]`
     - 否则更新 `right_max = height[right]`
     - `right -= 1`
3. 直到 `left == right`,返回 `ans`。

---

## 复杂度

- 时间复杂度: **O(n)** —— 左右指针各自最多走 n 步
- 空间复杂度: **O(1)** —— 只用了常数个变量

---

## 代码

见 [`42-trapping-rain-water.py`](./42-trapping-rain-water.py)
