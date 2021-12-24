from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = n - 1
            target = -nums[first]
            while second < third:
                if second > first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue
                if third < n - 1 and nums[third] == nums[third + 1]:
                    third -= 1
                    continue
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
                    second += 1
                elif nums[second] + nums[third] < target:
                    second += 1
                else:
                    third -= 1

        return ans

list = [0]
s = Solution()
print(s.threeSum(list))
