class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s = set()
        for i in range(len(nums)-1):
            check = nums[i]+nums[i+1]
            if check in s:
                return True 
            s.add(check)
        return False
