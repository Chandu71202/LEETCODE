class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s = list(s)
        for i in t:
            if s[0]==i:
                s.pop(0)
            if s==[]:
                return True
        return s==[]
        
