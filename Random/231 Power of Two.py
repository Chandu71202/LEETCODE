class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if( n <= 0 ):
            return False
        
        while( n%2 == 0 ):
            n = n / 2
        
        return [0,1][n==1]
