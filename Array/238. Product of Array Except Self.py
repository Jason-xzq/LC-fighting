# This solution is forbidden since it uses division

# Try next time please

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        zero = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(i)
        if len(zero) >= 2:
            return ret

        elif len(zero) == 1:
            nonzero = 1
            for i in range(len(nums)):
                if i != zero[0]:
                    nonzero *= nums[i]
            ret[zero[0]] = nonzero
            return ret
        else:
            first = 1
            for i in range(1, len(nums)):
                first *= nums[i]
            ret[0] = first

            for i in range(len(nums) - 1):
                ret[i + 1] = (ret[i] * nums[i] // nums[i + 1])
            return ret
