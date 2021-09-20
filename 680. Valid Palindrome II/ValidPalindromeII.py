class Solution:
    def validPalindrome(self, s: str) -> bool:
        def judge(left, right):
            i, j = left, right
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # if len(s) == 1 or len(s) == 2:
        #     return True

        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return judge(left+1, right) or judge(left, right-1)

        return True





s = Solution
string = "abc"

print(s.validPalindrome(s, string))