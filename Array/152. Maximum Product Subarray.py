from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSubMax = nums[0]
        curSubMin = nums[0]

        for i in range(1, len(nums)):
            tmp = curSubMax
            curSubMax = max(curSubMax * nums[i], curSubMin * nums[i], nums[i])
            curSubMin = min(tmp * nums[i], curSubMin * nums[i], nums[i])
            maxSub = max(maxSub, curSubMax)

        return maxSub

list = [-4, -3, -2]
s = Solution()
print(s.maxProduct(list))