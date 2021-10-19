class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator//denominator)
        res = []
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            res.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        res.append(str(numerator // denominator))
        res.append(".")
        remainder = numerator % denominator
        dict = {}
        while remainder and remainder not in dict:
            dict[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        if remainder:
            res.insert(dict[remainder], "(")
            res.append(")")
        return "".join(res)

s = Solution()
print(s.fractionToDecimal(-1, 333))

# print(-4//2)


