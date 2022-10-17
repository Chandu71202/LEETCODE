class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        
        if num==0:
            return 0
        
        for i in range(1,11):
            f=(i*k)%10
            if(f==num%10) and (num>=i*k):
                return i
        else:
            return -1
        
        
