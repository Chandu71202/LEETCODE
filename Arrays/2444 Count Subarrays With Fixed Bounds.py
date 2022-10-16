class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK:
            return 0
        
        out = 0
        
        bad = -1
        
        good1 = -1
        good2 = -1
        
        n = len(nums)
        for i in range(n):
            v = nums[i]
            
            if v < minK:
                bad =(i)
            elif v > maxK:
                bad=(i)
            else:
                if v == minK:
                    good1=(i)
                    
                if v == maxK:
                    good2=(i)
                    
                r = min(good1, good2)
                if r > bad:
                    out += r - bad
        return out
