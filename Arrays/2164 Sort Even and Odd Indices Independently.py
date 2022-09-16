class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        #110 ms
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
        
        # 114 ms
        # nums[::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2], reverse=True)
        # return nums
