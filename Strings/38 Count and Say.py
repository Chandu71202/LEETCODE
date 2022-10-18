class Solution:
    def countAndSay(self, n: int) -> str:
        x = "1"
        n-=1
        def helper(x):
            a = []
            for i,j in groupby(x):
                a.append(str(len(list(j)))+i)
            return "".join(a)
    
        while(n):
            x = helper(x)
            n-=1
        return x
