class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while(i <= j):
            pivot = (i + j) // 2
            if (nums[pivot] == target):
                return pivot
            elif (nums[pivot] > target):
                j = pivot - 1
            else:
                i = pivot + 1
        return i
            
