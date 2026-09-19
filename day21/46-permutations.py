from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue

                # 选择：把当前数字加入这条路径。
                path.append(num)
                used.add(num)

                backtrack()

                # 撤销选择：恢复现场，让当前层尝试下一个数字。
                path.pop()
                used.remove(num)

        backtrack()
        return result
