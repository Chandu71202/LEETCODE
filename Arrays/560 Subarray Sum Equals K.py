class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = { 0 : 1 }
        currSum = 0
        res = 0
        for i in nums:
            currSum+=i
            diff = currSum - k
            
            res += d.get(diff,0)
            d[currSum]=1+d.get(currSum,0)
        return res
