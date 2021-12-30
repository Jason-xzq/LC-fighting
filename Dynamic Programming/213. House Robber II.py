from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def sub(nums, start, end):
            s = end - start + 1
            if s == 1:
                return nums[start]
            first, second = nums[start], max(nums[start], nums[start + 1])
            for i in range(s - 2):
                third = max(first + nums[start + i + 2], second)
                first = second
                second = third
            return second

        s = len(nums)
        if s == 1:
            return nums[0]
        return max(sub(nums, 0, s - 2), sub(nums, 1, s - 1))


s = Solution()
nums = [1, 2, 3, 1]
print(s.rob(nums))