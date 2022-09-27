class Solution:
    def numberOfMatches(self, n: int) -> int:
        c=0
        while(n>1):
            if(n&1):
                c += int((n-1)/2)
                n = int((n-1)/2)+1
            else:
                c += int(n/2) 
                n = int(n/2)
        return c
