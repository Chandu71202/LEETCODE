class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while(i<len(nums)):
            x=nums.count(nums[i])
            if(x<3):
                i=i+1
                continue
            else:
                nums[i:i+x]=nums[i:i+2]
            i=i+1
