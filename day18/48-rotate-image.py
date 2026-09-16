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
