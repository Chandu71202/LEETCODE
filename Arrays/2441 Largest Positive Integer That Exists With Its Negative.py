class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        mx = -9999
        for i in nums:
            if i<0:
                if -1*i in nums:
                    mx = max(mx,-1*i)
        return -1 if mx==-9999 else mx
