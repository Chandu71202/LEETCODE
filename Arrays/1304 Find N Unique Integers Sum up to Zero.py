class Solution:
    def sumZero(self, n: int) -> List[int]:
        l=[]
        if n&1:
            l.append(0)
        i=0
        j=0
        while(n-2>=0):
            l.append(i-1)
            l.append(j+1)
            n-=2
            i-=1
            j+=1
        return l
