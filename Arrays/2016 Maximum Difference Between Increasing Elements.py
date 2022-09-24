class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)-1):
            mx = max(nums[i+1:])
            if(nums[i]<mx):
                ans = max(ans,mx - nums[i])
        return ans
