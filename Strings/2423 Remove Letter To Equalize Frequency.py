class Solution:
    def equalFrequency(self, word: str) -> bool:
        d={}
        for i in word:
            if d.get(i,-1)==-1:
                d[i]=1
            else:
                d[i]+=1
        for i in word:
            d[i]-=1
            l=[]
            for j in d.values():
                if j:
                    l.append(j)
            if len(set(l))==1:
                return True
            d[i]+=1
        return False
