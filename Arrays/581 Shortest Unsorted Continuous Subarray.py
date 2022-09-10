class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        x = sorted(nums)
        l = 0
        u = len(nums) - 1
        for i in range(len(nums)):
            if nums[i]!=x[i]:
                u=min(u, i)
                l=max(l, i)
        
        
        return 0 if u>=l else l-u+1
