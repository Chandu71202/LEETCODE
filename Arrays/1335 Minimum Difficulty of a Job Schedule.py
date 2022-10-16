class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        leng = len(jobDifficulty)
        
        if leng < d: 
            return -1
        
        elif leng == d: 
            return sum(jobDifficulty)
        
        dp = [[float('inf')] * (leng) for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        
        for i in range(1, leng):
            dp[0][i] = max(dp[0][i-1], jobDifficulty[i])
            
        for i in range(1, d):
            for j in range(i, leng):
                minDiff = 0
                for k in range(j, i-1, -1):
                    minDiff = max(minDiff, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i-1][k-1] + minDiff)
                    
        return dp[-1][-1]
