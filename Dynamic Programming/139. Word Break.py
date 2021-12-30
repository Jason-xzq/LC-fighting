class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict = {}
        for i in wordDict:
            dict[i] = True
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break
        return dp[len(s)]