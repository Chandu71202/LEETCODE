class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for c in range(len(nums)):
            if(nums[c]!=0):
                nums[k]=nums[c]
                k+=1
        nums[k:]=[0]*(len(nums)-k)
            
        
            
        
