class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n==2):
            return 1
        nums=[0,1]
        for i in range(n-1):
            nums.append(0)
            
        i=1
        while(2*i<n):
            nums[2*i]=nums[i]
            nums[2*i+1]=nums[i]+nums[i+1]
            i+=1
        return max(nums)
