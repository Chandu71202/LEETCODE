class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        for i in range(len(strs[0])):
            if(strs[0]!="" and len(strs[0])>=i):
                x=strs[0][i]
            else:
                x=""
            for j in range(1,len(strs)):
                if(strs[j]!="" and len(strs[j])>=i+1):
                    y=strs[j][i]
                else:
                    y=""
                if(x==y):
                    pass
                else:
                    return s
            s=s+x
        return s
                
