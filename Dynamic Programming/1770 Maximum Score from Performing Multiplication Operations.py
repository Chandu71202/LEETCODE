class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                left_choice = mult * nums[left] + dp[i + 1][left + 1]
                right_choice = mult * nums[right] + dp[i + 1][left]
                dp[i][left] = max(left_choice, right_choice)       
        return dp[0][0]
