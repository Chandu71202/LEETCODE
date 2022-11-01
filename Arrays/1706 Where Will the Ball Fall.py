class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res=[]
        for i in range(len(grid[0])):
            cpos=i
            npos=-1
            for j in range(len(grid)):
                npos=cpos+grid[j][cpos]
                if npos<0 or npos>=len(grid[0]) or grid[j][cpos]!=grid[j][npos]:
                    cpos=-1
                    break
                else:
                    cpos=npos
            res.append(cpos)
        return res
