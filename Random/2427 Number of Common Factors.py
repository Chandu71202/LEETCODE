class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c=0
        if a>b:
            n=a
        else:
            n=b
        for i in range(1,n+1):
            if(a%i==0 and b%i==0):
                c+=1
        return c
