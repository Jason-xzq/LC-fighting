class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            ans = [1, 2]
            i = 2
            while i != n:
                ans[i % 2] = ans[0] + ans[1]
                i += 1
            return ans[(n - 1) % 2]
