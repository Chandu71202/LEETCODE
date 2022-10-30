class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= (m + n - 2):
            return m + n - 2

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {(0, 0, k)}
        q = [(0, 0, k, 0)]
        while q:
            r, c, curr_k, curr_steps = q.pop(0)
            if (r, c) == (m - 1, n - 1):
                return curr_steps
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nk = curr_k - grid[nr][nc]
                    if nk >= 0 and (nr, nc, nk) not in visited:
                        visited.add((nr, nc, nk))
                        q.append((nr, nc, nk, curr_steps + 1))

        return -1
