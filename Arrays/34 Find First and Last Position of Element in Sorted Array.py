class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        c=0
        for i in range(len(nums)):
            if(target==nums[i]):
                l.append(i)
                c=c+1
        if(c==1):
            l.append(l[0])
            return l
        if(len(nums)==1 and target==nums[0]):
            return [0,0]
        if(l==[]):
            return [-1,-1]
        else:
            return [l[0],l[-1]]
        
