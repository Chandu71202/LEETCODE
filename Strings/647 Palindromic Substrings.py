## ITERATIVE

class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            left , right = i , i
            while left >=0 and right < len(s) and s[left]==s[right]:
                res +=1
                left-=1
                right+=1
            left , right = i , i+1
            while left >=0 and right < len(s) and s[left]==s[right]:
                res+=1
                left-=1
                right+=1
        return res

    
## RECURSIVE

class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        
        def helper(s,left,right):
            res=0
            while left >=0 and right < len(s) and s[left]==s[right]:
                res +=1
                left-=1
                right+=1
            return res
        
        for i in range(len(s)):
            res+=helper(s,i,i)
            res+=helper(s,i,i+1)
        return res
    
