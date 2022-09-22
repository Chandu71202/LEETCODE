class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {} 
        lose ={}
        for i in matches:
            win[i[0]]=0 
            lose[i[1]]=0
        for i in matches: 
            win[i[0]]+=1 
            lose[i[1]]+=1
        out1=[]
        for i in lose:
            if lose[i]==1: 
                out1.append(i) 
        out2=[]
        for i in win: 
            if i not in lose: 
                out2.append(i)
        return [sorted(out2),sorted(out1)]
