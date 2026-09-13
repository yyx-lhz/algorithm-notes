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
