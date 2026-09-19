# Day 23 · LeetCode 20. 有效的括号

**题目**: [LeetCode 20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/)

**标签**: 字符串 / 栈 / 哈希表 / Python3

---

## 我的思路

这道题用 `stack` 存还没有匹配的左括号。遇到左括号就先塞进去；遇到右括号，就看最近放进去的那个左括号能不能和它配对。最近的左括号要最先配对，所以正好用栈的“后进先出”。

遇到右括号时，如果栈已经是空的，说明没有左括号可以配对，直接返回 `False`；如果栈顶不是这个右括号对应的左括号，也返回 `False`。匹配成功才用 `stack.pop()` 把栈顶的左括号移除，表示这一对处理完了。

遍历结束以后，再看有没有全部配完：栈为空就返回 `True`；还有左括号剩下就返回 `False`。所以最后写 `return not stack`。

## mapping 的方向与 char 的含义

`char` 是遍历到的当前字符，可能是左括号，也可能是右括号。字典 `mapping` 的方向是 **右括号 → 对应左括号**：

```python
mapping = {
    ')': '(',
    ']': '[',
    '}': '{'
}
```

Python 的 `char in mapping` 检查的是字典的**键**。这里的键全部是右括号，因此：

- `char not in mapping`：当前字符不是右括号。题目保证输入只包含 `()[]{}`，所以它就是左括号，执行 `stack.append(char)`。
- 否则：当前字符是右括号，用 `mapping[char]` 找到它需要的左括号，与 `stack[-1]` 比较。

例如遇到 `)` 时，`mapping[')']` 得到 `'('`。右括号本身不入栈，它负责和栈顶的左括号配对。

## Python 3 代码

完整代码：[20-valid-parentheses.py](./20-valid-parentheses.py)。

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False

                stack.pop()

        return not stack
```

## 两个判断为什么这样写？

```python
if not stack or stack[-1] != mapping[char]:
    return False
```

`not stack` 表示栈为空。`or` 会短路：左边为真，就不再计算右边，因此不会在空栈上访问 `stack[-1]`。

只有栈非空且栈顶匹配时，才执行 `stack.pop()`。不能跳过栈顶去找更早的左括号，否则会把 `([)]` 这样的交叉括号错误地判成有效。

```python
return not stack
```

空列表在布尔判断中为 `False`，取反后为 `True`；非空列表在布尔判断中为 `True`，取反后为 `False`。这个返回必须放在 `for` 循环外，等所有字符处理完再检查。

## 这次的缩进问题

`stack.pop()` 必须在 `else` 内部，并且放在不匹配判断之后，与里面的 `if` 对齐：

```text
for 每个字符:
    if 左括号:
        入栈
    else: 右括号
        if 栈为空或不匹配:
            return False
        pop：移除已经匹配的左括号
循环结束后 return not stack
```

如果把 `pop()` 放到 `else` 外面，遇到左括号时就会刚入栈又立刻出栈，后面的右括号自然找不到对应的左括号。匹配成功时是“把左括号 pop 出来”，不是“pop 不出来”。

## 跟着例子走一遍

以 `s = "([])"` 为例，栈顶在右侧：

| 当前字符 | 操作 | 操作后的 stack |
|----------|------|----------------|
| `(` | 左括号，入栈 | `['(']` |
| `[` | 左括号，入栈 | `['(', '[']` |
| `]` | 栈顶是 `[`，匹配并 pop | `['(']` |
| `)` | 栈顶是 `(`，匹配并 pop | `[]` |

遍历结束，栈为空，`return not stack` 得到 `True`。

## 示例自查

| s | 结果 | 原因 |
|---|------|------|
| `"()"` | `True` | 一对括号匹配 |
| `"()[]{}"` | `True` | 多组括号依次匹配 |
| `"([])"` | `True` | 嵌套顺序正确 |
| `"(]"` | `False` | 括号类型不匹配 |
| `"([)]"` | `False` | 当前右括号与栈顶不匹配 |
| `")"` | `False` | 遇到右括号时栈为空 |
| `"("` | `False` | 遍历结束仍有左括号剩余 |
| `"())"` | `False` | 多出一个右括号 |

## 复杂度

设 `n = len(s)`。

- 时间复杂度：**O(n)**，每个字符处理一次，每个左括号最多入栈、出栈各一次。
- 辅助空间复杂度：**O(n)**，最坏情况下全部是左括号，都需要存入栈；`mapping` 只有三组对应关系，占用常数空间。
