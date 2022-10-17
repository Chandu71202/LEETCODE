class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        d = defaultdict(list)
        for i,num in enumerate(nums):
            d[num].append(i)
        
        for key,value in d.items():
            if len(value)>1:
                for i in range(1,len(value)):
                    if abs(value[i]-value[i-1])<=k:
                        return True
                    
        return False
