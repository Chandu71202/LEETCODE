class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if(nums[i]==nums[i-1]):
        #         return nums[i]
        set1=set()
        for i in nums:
            if i in set1:
                return i
            set1.add(i)
