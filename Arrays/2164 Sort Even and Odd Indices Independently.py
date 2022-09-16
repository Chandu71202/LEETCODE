class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for i in range(len(nums)):
            if(i&1==0):
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        l1.sort()
        l2.sort()
        l = []
        while(l1 and l2):
            l.append(l1.pop(0))
            l.append(l2.pop())
        l+=l1
        l+=l2
        return l
