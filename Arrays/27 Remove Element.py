class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=len(nums)
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            if(nums[0]==val):
                return 0
            else:
                return 1
        while(c!=0):
            if(val==nums[c-1]):
                nums.remove(nums[c-1])
            c=c-1
        return len(nums)
