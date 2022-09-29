class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        l = nums[:]
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                nums.pop(i)
                l.pop(i+1)
                break
        if(nums==sorted(list(set(nums))) or l==sorted(list(set(l))) ):
            return True
        else:
            return False
        return True
