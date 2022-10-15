class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
            
        
        ans = nums[0]
        for ind, s in enumerate(prefix_sum):
            ans = max(ans, int(math.ceil(s / (ind + 1))))
            
        return ans
            
            
        
