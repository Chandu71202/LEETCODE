class Solution:
    def greatestLetter(self, s: str) -> str:
        # 225ms
        
        # up = []
        # low = []
        # for i in s:
        #     if i.islower():
        #         low.append(i.upper())
        #     else:
        #         up.append(i)
        # dup = []
        # for i in low:
        #     if i in up:
        #         dup.append(i)
        # return "" if dup==[] else sorted(dup)[-1]
        
        #57ms
        l = []
        for i in s:
            if(i.upper() in s and i.lower() in s):
                l.append(i.upper())
        if len(l) == 0:
            return ""
        return max(l)
