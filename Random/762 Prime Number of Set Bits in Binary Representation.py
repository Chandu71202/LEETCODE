class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime(n):
            if(n==0 or n==1):
                return False
            if(n==2 or n==3):
                return True
            for i in range(2,n//2+1):
                if(n%i==0):
                    return False
            else:
                return True
        c=0
        for i in range(left,right+1):
            if(prime(bin(i)[2:].count('1'))):
                c+=1
        return c
