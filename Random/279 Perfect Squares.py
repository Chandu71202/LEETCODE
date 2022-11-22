@lru_cache(None)
def dp(n: int) -> int:
    return 0 if n == 0 else min(dp(n-(x+1)**2) for x in range(floor(sqrt(n)))) + 1
class Solution:
    def numSquares(self, n: int) -> int:
        return dp(n)
