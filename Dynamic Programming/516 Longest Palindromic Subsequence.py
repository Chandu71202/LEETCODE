class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2=s[::-1]
        dp=[]
        for i in range(len(s2)+1):
            q=[0 for j in range(len(s)+1)]
            dp.append(q)
        mx=0
        for i in range(1,len(s2)+1):
            for j in range(1,len(s)+1):
                if(s2[i-1]==s[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[i][j]
