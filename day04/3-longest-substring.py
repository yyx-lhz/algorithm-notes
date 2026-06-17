from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter()
        left = 0

        for right, c in enumerate(s):
            cnt[c] += 1

            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # 3
    print(sol.lengthOfLongestSubstring(""))          # 0
