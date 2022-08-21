class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        def length(n):
            l=nums.index(n)
            h=nums[::-1].index(n)
            return len(nums[l:len(nums)-h])
        mx=0
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        mx=max(d.values())
        b=[]
        for i,j in reversed(sorted(d.items(),key=lambda x:x[1])):
            if(mx==j):
                b.append(i)
        mx=9999999
        for i in b:
            mx=min(mx,length(i))
        return mx

