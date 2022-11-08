class Solution:
    def makeGood(self, s: str) -> str:
        
        i = 0
        while(i >= 0 and i < len(s)-1):
            if s[i].lower() == s[i+1].lower() and ( (s[i].islower() and s[i+1].isupper()) or (s[i].isupper() and s[i+1].islower()) ):
                s = s[:i] + s[i+2:]
                i -= 1
            else:
                i += 1
            if i < 0:
                i = 0
        return s
