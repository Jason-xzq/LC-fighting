import copy
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        res = []
        while x != 0:
            digit = x % 10
            res.append(digit)
            x = x // 10
        res2 = copy.deepcopy(res)
        res2.reverse()
        for i in range(len(res)):
            # print(res[i])
            if res[i] != res2[i]:
                return False
        return True

x = 121
s = Solution
print(s.isPalindrome(s,x))
