class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            if grid[r][0]==0:
                for c in range(COLS):
                        grid[r][c]=(grid[r][c]+1)%2
                        
        for c in range(COLS):
            count = 0
            for r in range(ROWS):
                count += 1 if grid[r][c] else 0
            if count <= ROWS // 2:
                for r in range(ROWS):
                    grid[r][c]=(grid[r][c]+1)%2
        
        ans = 0
        for r in range(ROWS):
            s="0b"
            for c in range(COLS):
                s+=str(grid[r][c])
            ans+=int(s,2)
        
        return ans
        
