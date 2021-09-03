from typing import List
import copy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cpy = copy.deepcopy(nums)
        cpy.sort()
        head = 0
        tail = len(nums) - 1
        result = []
        while True:
            if(cpy[head]+cpy[tail]==target):
                left = cpy[head]
                right = cpy[tail]
                break
            elif (cpy[head]+cpy[tail]<target):
                head += 1
            else:
                tail -= 1
        for i in range(len(nums)):
            if(nums[i] == left):
                result.append(i)
                break
        for j in range(len(nums)):
            if(nums[j] == right and j != i):
                result.append(j)
                break
        return result

        # step = 1
        # while head < len(nums)-1:
        #     if(head + step > len(nums)-1):
        #         head += 1
        #         step = 1
        #         continue
        #     if(nums[head]+nums[head+step]==target):
        #         return [head, head+step]
        #     else:
        #         step += 1


nums = [-1, -2, -3, -4, -5]
target = -8
# print(type(nums))
s = Solution()
print(s.twoSum(nums, target))