class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        c=0
        for i in nums: 
            if i&1==0:
                c+=i 
        l = [] 
        for i in queries:
            prev = nums[i[1]]
            nums[i[1]]=nums[i[1]]+i[0]
            if prev&1==0: 
                c-=prev 
            if nums[i[1]]&1==0: 
                c+=nums[i[1]]
            l.append(c) 
        return l
