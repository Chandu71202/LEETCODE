class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i, x in enumerate(nums[:-2]):
            if x < nums[i+1] + nums[i+2]:
                return x + nums[i+1] + nums[i+2]
        return 0
