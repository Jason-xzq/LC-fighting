from typing import List
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        min = sys.maxsize
        for i in prices:
            if i - min > max:
                max = i - min
            if i < min:
                min = i
        return max


        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > max:
        #             max = prices[j] - prices[i]
        # return max

prices = [7,1,5,3,6,4]
s = Solution
print(s.maxProfit(s, prices))