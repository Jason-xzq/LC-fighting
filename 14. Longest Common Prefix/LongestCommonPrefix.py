from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in strs:
            if i == "":
                return ""
        left = 0
        right= 0
        flag = 1
        while True:
            if right >= len(strs[0]):
                break
            tmp = strs[0][right]
            for i in strs:
                if right >= len(i):
                    flag = 0
                    break
                if tmp != i[right]:
                    flag = 0
                    break

            if flag == 1:
                right += 1

            if flag == 0:
                break

        return strs[0][left:right]

strs = ["dog","racecar","car"]
s = Solution
print(s.longestCommonPrefix(s, strs))

