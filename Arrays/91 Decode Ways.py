class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0": return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i, c in enumerate(s[1:], 1):
            if c >= "1" and c <= "9": 
                dp[i+1] = dp[i] 
            if s[i-1:i+1] and s[i-1:i+1] <= "26" and s[i-1:i+1] >= "10" : 
                dp[i+1] += dp[i-1]
            
        return dp[-1]
