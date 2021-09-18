class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in range(len(s)):
            if s[i] in dict:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if dict[stack.pop()] != s[i]:
                    return False
        if len(stack) != 0:
            return False
        return True

x = "["
s = Solution
print(s.isValid(s, x))