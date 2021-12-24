from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left != mid:
            if nums[mid] > nums[right]:
                left = mid
                mid = (left + right) // 2
            else:
                right = mid
                mid = (left + right) // 2
        if nums[left] > nums[right]:
            return nums[right]
        else:
            return nums[left]


list = [3, 4, 5, 1, 2]
s = Solution()
print(s.findMin(list))