class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        #RUNTIME : 46ms
        s1=list(map(str,s1.split()))
        s2=list(map(str,s2.split()))
        l=[]
        for i in s1:
            if i not in s2:
                l.append(i)
        for i in s2:
            if i not in s1:
                l.append(i)
        s=[]
        for i in l:
            if l.count(i)==1:
                s.append(i)
        return s
        
        # RUNTIME : 62ms
#         s1 = s1.split(' ') + s2.split(' ')
#         d = {}

#         for i in s1:
#           if i in d:
#             d[i] += 1
#           else:
#             d[i] = 1

#         res = []

#         for i in d:
#           if d[i] == 1:
#             res.append(i)
#         return res
