from typing import List
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = -sys.maxsize - 1
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp > max:
                max = tmp
            if tmp < 0:
                tmp = 0

        return max

nums = [5,4,-1,7,8]
s = Solution
print(s.maxSubArray(s,nums))

