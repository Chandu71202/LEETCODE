class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        elif(n==1):
            return 1
        l=[]
        a=0
        b=1
        l.append(a)
        l.append(b)
        for i in range(n-1):
            c=a+b
            a=b
            b=c
            l.append(c)
        return l[-1]
