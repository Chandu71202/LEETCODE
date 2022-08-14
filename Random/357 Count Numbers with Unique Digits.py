class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        init=2
        if n==0:
            return 1
        elif n==1:
            return 10
        else:
            out=10
            while(init<=n):
                inout=9
                count=9
                for i in range(1,init):
                    inout*=count
                    count-=1
                out+=inout
                init+=1
            return out
                 


            
