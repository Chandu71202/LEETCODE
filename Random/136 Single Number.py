class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if d.get(i,-1)==-1:
                d[i]=1
            else:
                d[i]+=1
        for key,value in d.items():
            if value==1:
                return key
