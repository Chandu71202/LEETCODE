class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
        ans = []
        begin = 0
        for i,j in logs:
            ans.append(j-begin)
            begin = j
            
        ind = []
        mx = max(ans)
        for i in range(len(ans)):
            if mx==ans[i]:
                ind.append(i)
                
        for i in range(len(ind)):
            ind[i] = logs[ind[i]][0]
        
        return min(ind)
        
