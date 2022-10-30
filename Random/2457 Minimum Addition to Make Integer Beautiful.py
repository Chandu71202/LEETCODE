class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        i=n
        l=1
        while i<=10**12:
            s=0
            for j in str(i):
                s+=int(j)
            if s<=target:
                return i-n
            i//=10**l
            i+=1
            i*=10**l
            l+=1
