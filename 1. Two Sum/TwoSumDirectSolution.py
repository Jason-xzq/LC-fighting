from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return[i, j]



nums = [-1, -2, -3, -4, -5]
target = -8
# print(type(nums))
s = Solution()
print(s.twoSum(nums, target))