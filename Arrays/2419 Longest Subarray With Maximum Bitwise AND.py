class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        c = 0
        ans = 1
        for i in nums:
            if i == mx:
                c += 1
            else:
                c = 0
            ans = max(ans, c)
        
        return ans
