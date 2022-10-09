class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        s = set(nums)
        counts = []
        mx = 0
        for i in s:
            if i%2==0:
                counts.append(i)
        if counts==[]:
            return -1
        counts=sorted(counts)
        print(counts)
        mx = 0
        ans = 0
        for i in counts:
            if nums.count(i)>mx:
                mx = nums.count(i)
                ans = i
        return ans
