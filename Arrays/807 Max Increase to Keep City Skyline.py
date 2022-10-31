class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                column = max([grid[k][j]] for k in range(len(grid)))
                ans += (min(column[0], max(grid[i])) - grid[i][j])
        return ans
