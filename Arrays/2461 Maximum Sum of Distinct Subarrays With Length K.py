class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        ctr = Counter()
        curr = 0
        max_sum = -math.inf
        
        for r in range(len(nums)):
            ctr[nums[r]] += 1
            curr += nums[r]
            
            while ctr[nums[r]] > 1 or (r - l + 1) > k:
                curr -= nums[l]
                ctr[nums[l]] -= 1
                l += 1
            
            if (r - l + 1) == k:
                max_sum = max(max_sum, curr)
            
        return max_sum if max_sum != -math.inf else 0    
