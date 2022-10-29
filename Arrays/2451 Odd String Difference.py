class Solution:
    def oddString(self, words: List[str]) -> str:
        req = []
        req1 = []
        for i in range(len(words)):
            temp = []
            for j in range(1,len(words[i])):
                temp.append(ord(words[i][j])-ord(words[i][j-1]))
            req.append((words[i],temp))
            req1.append(temp)
        for i in req1:
            if req1.count(i)==1:
                ans = i
        for i in req:
            if i[1]==ans:
                return i[0]
