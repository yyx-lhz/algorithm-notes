class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_size = 0
        right_size = len(height) - 1
        area = 0
        while left_size < right_size:
            current_area = (right_size - left_size) * min(
                height[left_size], height[right_size]
            )
            if height[left_size] > height[right_size]:
                right_size -= 1
            else:
                left_size += 1
            area = max(current_area, area)
        return area


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # 49
