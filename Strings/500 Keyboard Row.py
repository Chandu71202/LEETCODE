class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        one = "qwertyuiopQWERTYUIOP"
        two = "asdfghjklASDFGHJKL"
        three = "zcvbnmZXCVBNM"
        ans = []
        for i in words:
            a = []
            for x in i:
                if x in one:
                    c=1
                elif x in two:
                    c=2
                else:
                    c=3
                if a==[]:
                    a.append(c)
                elif a[-1]!=c:
                    break
            else:
                ans.append(i)
        return ans
                
