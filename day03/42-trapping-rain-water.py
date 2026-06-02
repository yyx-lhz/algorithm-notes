class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        ans = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    ans += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    ans += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # 6
