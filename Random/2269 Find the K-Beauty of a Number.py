class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        c = 0
        numStr = str(num)
        for i in range(len(numStr)-k+1):
            s = int(numStr[i:i+k])
            if s!=0 and num%s==0:
                c+=1 
        return c
            
