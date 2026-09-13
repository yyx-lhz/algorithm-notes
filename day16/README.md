# Day 16 · LeetCode 49. 字母异位词分组

## 我的思路

遍历所有字符串，把当前字符串里的字符排序，得到一个分组用的 key。如果 group 里面已经有这个 key，就把当前字符串加到对应的组里；如果没有，就先创建一个新组，再把字符串加进去。最后返回所有分组。

具体来说，边遍历边排序、边分组即可，不需要先把所有字符串遍历完，也不需要两两比较。

## 为什么可以这样分组

字母异位词的字符种类和每种字符的数量相同，所以排序后得到的字符串相同。例如 `eat`、`tea`、`ate` 排序后都是 `aet`，因此使用同一个 key，放进同一个组。

- `k = ''.join(sorted(s))`：把排序结果转换成字符串，作为字典的 key。
- `group[k]`：保存这一组的原始字符串列表。
- key 不存在时执行 `group[k] = []`，创建新组。
- 随后执行 `group[k].append(s)`，把当前原始字符串加入组中。
- 最后用 `list(group.values())` 返回所有组。

## 例子

输入：`["eat", "tea", "tan", "ate", "nat", "bat"]`

| 遍历到的字符串 | 排序后的 key | 操作后的对应分组 |
|---|---|---|
| eat | aet | [eat] |
| tea | aet | [eat, tea] |
| tan | ant | [tan] |
| ate | aet | [eat, tea, ate] |
| nat | ant | [tan, nat] |
| bat | abt | [bat] |

返回：`[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`。分组顺序不影响答案。

## Python 3 代码

完整代码：[49-group-anagrams.py](./49-group-anagrams.py)。

```python
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            k = ''.join(sorted(s))
            if k not in group:
                group[k] = []
            group[k].append(s)

        return list(group.values())
```

## 容易混淆的地方

1. `sorted(s)` 返回列表，列表不能直接作为字典的 key；用 `''.join(...)` 转成字符串即可。
2. 排序后的 k 只用于识别分组，加入列表的应该是原始字符串 s。
3. key 已存在时要 append，不能重新赋值为空列表，否则会丢失已经分好的字符串。
4. 空字符串排序后仍是空字符串，可以正常作为 key；重复字符串也要逐个保留。

## 复杂度

设字符串数量为 n，最大字符串长度为 m。

- 时间：O(n · m log m)，主要来自每个字符串的字符排序（m ≥ 2 时的通常写法）。
- 空间：O(n · m + n)，用于分组 key、各组的字符串引用及排序临时空间；原始字符串本身没有被复制。
