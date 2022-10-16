class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        
        while(i<n):
            nums.append(int(str(nums[i])[::-1]))
            i+=1
        return len(set(nums))
