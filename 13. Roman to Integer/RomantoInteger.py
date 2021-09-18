class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM':900}

        list = []

        left = 0
        right = 1
        while left < len(s):
            if s[left] == 'I' or s[left] == 'X' or s[left] == 'C':
                if s[left:(right+1)] in dict:
                    right += 1
            list.append(s[left:right])
            left = right
            right += 1
        res = 0
        for i in list:
            res += dict[i]

        return res

s = Solution
print(s.romanToInt(s, "MCMXCIV"))


