class Solution:
    def rob(self, nums: List[int]) -> int:
        s = len(nums)
        if s == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(s - 2):
            third = max(first + nums[i + 2], second)
            first = second
            second = third
        return second
