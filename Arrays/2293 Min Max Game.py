class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while(len(nums)>1):
            min_max=[]
            flag = True
            for i in range(0,len(nums),2):
                if flag:
                    min_max.append(min(nums[i:i+2]))
                    flag=False
                else:
                    min_max.append(max(nums[i:i+2]))
                    flag=True
            nums = min_max
        return nums[0]
                    
