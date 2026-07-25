from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left() -> int:
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    answer = mid
                    right = mid - 1

            return answer

        def find_right() -> int:
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    answer = mid
                    left = mid + 1

            return answer

        return [find_left(), find_right()]


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
    print(sol.searchRange([], 0))                   # [-1, -1]
    print(sol.searchRange([1], 1))                  # [0, 0]
