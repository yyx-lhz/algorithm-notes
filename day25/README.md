# Day 25 · LeetCode 200：岛屿数量

## 核心思路

遍历整个 grid，遇到尚未访问的 `'1'` 就 `count += 1`，然后用 DFS 把这座岛上所有相连的 `'1'` 标记成 `'0'`。

岛屿只按上下左右相连，对角线不算。每次 DFS 会“淹掉”一整座岛，因此后续遍历不会重复计数。

## 步骤

1. 初始化岛屿数量 `count = 0`。
2. 双重循环遍历每个格子。
3. 如果当前格是 `'1'`，说明发现一座新岛，计数加一并调用 DFS。
4. DFS 先检查是否越界或为水；否则先把当前格设为 `'0'`，再向上下左右递归。
5. 遍历结束，返回 `count`。

## DFS 边界条件

以下任意条件成立就 `return`：

- 行越界：`r < 0 or r >= rows`。
- 列越界：`c < 0 or c >= cols`。
- 当前格是水或已经访问：`grid[r][c] == '0'`。

必须先判断越界，再访问 `grid[r][c]`；Python 的 `or` 短路求值会在越界时跳过后面的访问。

## Python 3 模板代码

```python
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == '0'
            ):
                return

            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count
```

## 时间 / 空间复杂度

设网格有 m 行、n 列。

- **时间 O(mn)**：遍历全部格子，每个陆地格最多被标记一次，每次只检查四个方向。
- **额外空间 O(mn)**：最坏情况下递归调用栈深度达到 O(mn)。虽然原地标记、不需要 visited 数组，但递归栈仍占空间。

## 易错点

- **缩进**：标记和四次递归应与 `if` 对齐，不能写在 `return` 后面的同一 if 块中，否则不会执行。
- **行列别写混**：`r` 与 `rows` 比较，`c` 与 `cols` 比较；不要把 `c >= cols` 写成 `r >= cols`。
- **先标记，再递归**：否则相邻陆地会互相反复访问。
- **字符类型**：使用 `'1'`、`'0'`，不是整数 `1`、`0`。
- **计数位置**：只在外层遍历发现新岛时加一，不能在 DFS 中每遇到一个陆地格就加一。
- **原地修改**：该写法会改变输入 grid；需要保留原数据时，先复制每一行。
- **递归深度**：大岛可能触发 Python 的 `RecursionError`；较大输入可改用显式栈的迭代 DFS 或 BFS。
- **空网格**：先检查空输入，再读取 `grid[0]`。

> 复习口诀：遇到 1，岛加一；先判界，再标记；上下左右淹到底。

