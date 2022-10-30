class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d = {}
        n = len(views)
        for i in range(n):
            if d.get(creators[i],-1)==-1:
                d[creators[i]]=[views[i],ids[i],views[i]]
            else:
                d[creators[i]][0]+=views[i]
                if d[creators[i]][2]<views[i]:
                    d[creators[i]][2]=views[i]
                    d[creators[i]][1]=ids[i]
                elif d[creators[i]][2]==views[i]:
                   if d[creators[i]][1]>ids[i]:
                        d[creators[i]][1]=ids[i]
        mx = 0
        for i in d:
            mx = max(mx,d[i][0])
        ans = []
        for i in d:
            if d[i][0]==mx:
                ans.append([i,d[i][1]])
        return ans
