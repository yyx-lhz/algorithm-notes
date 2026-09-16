# Day 18 · LeetCode 48. 旋转图像

## 解题思路

对 n × n 方阵，先转置，再将每一行左右反转，就能原地顺时针旋转 90°。

1. 转置：交换 `matrix[i][j]` 和 `matrix[j][i]`。内层从 `i + 1` 开始，跳过主对角线，并保证每对元素只交换一次，避免换回原样。
2. 每行反转：对每一行调用 `row.reverse()`，原地反转这一行。

位置变化为 `(i, j) → (j, i) → (j, n - 1 - i)`，正好是顺时针旋转 90°。

## 例子

```text
原矩阵       转置后       每行反转后
1 2 3        1 4 7        7 4 1
4 5 6   →    2 5 8   →    8 5 2
7 8 9        3 6 9        9 6 3
```

## 易错点

- 顺序是“转置 → 每行反转”，只需要这两步，不需要再反转每一列。
- `matrix[i][j] = matrix[j][i]` 只是覆盖，会丢失原值。交换要写成 `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`，Python 会先计算右边的两个原值，再赋值。
- 不要遍历所有 `(i, j)` 来交换，否则同一对元素交换两次后会回到原位。
- `row.reverse()` 直接修改当前行，方法无需返回矩阵。

## Python 3 代码

完整代码：[48-rotate-image.py](./48-rotate-image.py)。

```python
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 转置：沿主对角线交换，每对元素只交换一次。
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 每一行左右反转，完成顺时针旋转 90°。
        for row in matrix:
            row.reverse()
```

## 边界与复杂度

- 1 × 1 矩阵旋转后不变；奇数和偶数边长都适用。
- 时间：O(n²)，转置和每行反转均需要处理矩阵中的元素。
- 额外空间：O(1)，不创建新矩阵，只使用固定数量的辅助变量。
