# nums = [-1, -2, -3, -4, -5]
# hashtable = dict()
# hashtable['Age'] = 24
# hashtable['Name'] = 'Jason'
# print(hashtable['Name'])
# print(hashtable['Age'])

# a = "Jason"
# print(type(a))
# b = 'jason'
# print(type(b))
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            if target-num in hashtable:
                return[hashtable[target-num], i]
            hashtable[num] = i


nums = [-1, -2, -3, -4, -5]
target = -8
# print(type(nums))
s = Solution()
print(s.twoSum(nums, target))

