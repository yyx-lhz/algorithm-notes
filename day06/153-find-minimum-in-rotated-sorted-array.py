class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                # 右侧有序，最小值在左侧（含 mid）
                right = mid
            else:
                # nums[mid] > nums[right]，断崖在右侧，最小值在 mid 右边
                left = mid + 1

        # left == right 时即为最小值位置
        return nums[left]
