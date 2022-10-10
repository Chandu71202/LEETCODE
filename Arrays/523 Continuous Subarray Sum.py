class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = { 0 : -1}
        total = 0
        
        for i,n in enumerate(nums):
            total+=n
            r = total%k
            
            if r not in d:
                d[r]=i
            elif i-d[r]>1:
                return True
            
        return False
