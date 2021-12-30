from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        for i in range(len(nums)):
            if i > right:
                continue
            right = max(i+nums[i], right)
            if right >= len(nums)-1:
                return True
        return False


s = Solution()
nums = [3,2,1,0,4]
print(s.canJump(nums))


