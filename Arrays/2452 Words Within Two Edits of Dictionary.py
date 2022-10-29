class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def func(i,j):
            count = 0
            for z in range(len(i)):
                if count>2:
                    return False
                if i[z]!=j[z]:
                    count+=1
            if count<=2:
                return True
            return False
        
        res = []
        for i in queries:
            for j in dictionary:
                if func(i,j)==False:
                    continue
                else:
                    res.append(i)
                    break
        return res
