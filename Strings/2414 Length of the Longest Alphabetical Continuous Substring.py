class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        mx = 1
        c = 1
        for i in range(len(s)-1):
            if(ord(s[i])+1==ord(s[i+1])):
                c+=1
            else:
                mx = max(mx,c)
                c=1
            mx=max(mx,c)
        return mx
                
