class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        for i in range(2,n):
            for j in range(i+1,n+1):
                a = (i*i+j*j)**0.5 
                if(int(a)==a and a<=n):
                    c+=2 
        return c
