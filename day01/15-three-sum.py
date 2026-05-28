class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            k = i + 1
            j = len(nums) - 1
            while k < j:
                s = nums[i] + nums[k] + nums[j]
                if s > 0:
                    j -= 1
                elif s < 0:
                    k += 1
                else:
                    res.append((nums[i], nums[k], nums[j]))
                    while k < j and nums[k] == nums[k + 1]:
                        k += 1
                    while k < j and nums[j] == nums[j - 1]:
                        j -= 1
                    k += 1
                    j -= 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    # [(-1, -1, 2), (-1, 0, 1)]
