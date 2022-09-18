class Solution:
    def trap(self, height: List[int]) -> int:
        i, j, ans, mx, mi = 0, len(height) - 1, 0, 0, 0
        while i <= j:
            mi = min(height[i], height[j])
            mx = max(mx, mi)
            ans += mx - mi
            if height[i] < height[j]: i += 1
            else: j -= 1
        return ans
