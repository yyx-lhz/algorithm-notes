class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 判断哪一段有序
            if nums[left] <= nums[mid]:
                # 左半段有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1      # target 在左半段
                else:
                    left = mid + 1        # target 在右半段
            else:
                # 右半段有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1        # target 在右半段
                else:
                    right = mid - 1       # target 在左半段

        return -1
