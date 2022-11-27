class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        output = 0
        for i in range(n):
            for j in range(i):
                difference = nums[i] - nums[j]
                output += dp[j][difference]
                dp[i][difference] += 1 + dp[j][difference]
        
        return output
