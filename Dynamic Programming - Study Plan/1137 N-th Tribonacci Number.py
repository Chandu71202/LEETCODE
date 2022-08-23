class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        a=0
        b=1
        c=1
        l=[]
        l.append(a)
        l.append(b)
        l.append(c)
        for i in range(n-2):
            d=a+b+c
            l.append(d)
            a=b
            b=c
            c=d
            d=a
        return l[-1]
