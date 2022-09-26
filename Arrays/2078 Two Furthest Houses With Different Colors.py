class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        if(len(colors)==2):
            return 1
        if colors[0]!=colors[-1]:
            return len(colors)-1
        dis = 0
        for i in range(len(colors)):
            if colors[i] != colors[0]:
                dis = max(dis,i)
            if colors[i] != colors[-1]:
                dis = max(dis,len(colors)-1-i)
        return dis
