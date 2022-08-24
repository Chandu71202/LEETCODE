class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
        	return False
        
        while n % 3 == 0:        	
        	n = n / 3
           
#         return [0,1][n==1]
        return True if n == 1 else False
