class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum1 = 0
        n = 0
        for i in nums:
            if i%3==0 and i%2==0:
                sum1+=i
                n+=1
        return sum1//n if n!=0 else 0
