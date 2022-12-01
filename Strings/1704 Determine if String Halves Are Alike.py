class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        s1 = s[:n//2]
        s2 = s[n//2:]
        vow = "aeiouAEIOU"
        c1 = 0
        c2 = 0
        for i in s1:
            if i in vow:
                c1+=1
        for i in s2:
            if i in vow:
                c2+=1
        return c1==c2
        
