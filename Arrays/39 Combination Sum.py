class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp=[[] for i in range(target+1)]
        dp[0]=[[]]
        for i in candidates:
            for j in range(i,target+1):
                for k in dp[j-i]:
                    dp[j].append(k+[i])
        return dp[-1]
        
