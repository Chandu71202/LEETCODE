class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(set(colors))==len(colors):
            return 0
        d = {}
        for i in range(len(colors)):
            if d.get(colors[i],-1)==-1:
                d[colors[i]]=[i]
            else:
                d[colors[i]].append(i)
        ans = 0
        for i in d.values():
            for j in range(1,len(i)):
                if i[j-1]+1 == i[j]:
                    ans += min(neededTime[i[j-1]],neededTime[i[j]])
                    neededTime[i[j]]=max(neededTime[i[j-1]],neededTime[i[j]])
        return ans
                    
