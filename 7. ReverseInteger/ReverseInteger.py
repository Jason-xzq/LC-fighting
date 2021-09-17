class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        res = 0

        while (x != 0):
            if res < MIN // 10 + 1 or res > MAX // 10:
                return 0
            digit = x % 10
            if digit > 0 and x < 0:
                digit -= 10

            res = res * 10 + digit

            x = (x - digit) // 10

        return res

x = -123
s = Solution
print(s.reverse(s, x))

# x = [1, 2, 3]
# for i in range(2, -1, -1):
#     print(x[i])