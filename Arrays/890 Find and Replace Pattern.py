class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]: 
        ans = []
        for i in words:
            c=0
            d1 = {}
            for j in range(len(i)):
                if pattern[j] not in d1:
                    d1[pattern[j]] = i[j]
                elif d1[pattern[j]]!=i[j]:
                    c=1
                    break
            if(c==0):
                ans.append(i)
        res = []
        for i in ans:
            if len(set(i))==len(set(pattern)):
                res.append(i)
        return res
