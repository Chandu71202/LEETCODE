class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        l=list(map(str,s.split()))
        if(len(l)!=len(pattern)):
            return False
        i=0
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]]=l[i]
            elif d[pattern[i]]==l[i]:
                continue
            else:
                return False
            l1=[]
        for i in d:
            l1.append(d[i])
        if(len(set(l1)))!=len(d):
            return False
        return True
            
