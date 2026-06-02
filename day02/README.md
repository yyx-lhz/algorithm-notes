# Day 02 · 2026-06-03

**题目**: [LeetCode 11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)

**标签**: 数组 / 双指针 / Python3

---

## 思路

**你选用何种方法解题?**

暴力解就是随便找两个、两两配对,$O(n^2)$,但是不行。优化一下可以用**双指针**。

怎么用双指针呢?就是先固定一个,比如求两数和,就是先排序,大了就调小的、不用管大的;小了就调大的、不用管小的。接雨水是固定一边不用管,因为那边肯定可以兜住。

这题比较相似:要动一边的话,问最大的接水,就是选择最大的那个。怎么变大呢?**肯定变短的那一边**。

为什么?因为移动高的那一边,宽度变小,**短板效应**下短板不变,宽度变小,所以面积一定变小。只有移动短的那一边,才能找到更高的板,从而抵消宽度的减小,**并逆袭成功!奥利给!!!**

---

## 解题过程

1. 左右两个指针 `left_size` 和 `right_size`,从两端往中间走。
2. 每次计算当前面积:`current_area = (right_size - left_size) * min(height[left_size], height[right_size])`。
3. **移动短板**:
   - 如果 `height[left_size] > height[right_size]`,右指针更短 → `right_size -= 1`
   - 否则左指针更短或相等 → `left_size += 1`
4. 用 `area = max(current_area, area)` 维护历史最大值。

---

## 复杂度

- 时间复杂度: **O(n)** —— 双指针各自最多走 n 步
- 空间复杂度: **O(1)** —— 只用了常数个变量

---

## 代码

见 [`11-container-with-most-water.py`](./11-container-with-most-water.py)
