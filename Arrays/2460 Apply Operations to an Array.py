class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                nums[i-1]=nums[i-1]*2
                nums[i]=0
        c = nums.count(0)
        for i in range(c):
            nums.remove(0)
        return nums+c*[0]
