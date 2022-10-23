class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = n*(n+1)//2 - sum(set(nums))
        nums.sort()
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                ans = nums[i]
                break
        return [ans,res]
