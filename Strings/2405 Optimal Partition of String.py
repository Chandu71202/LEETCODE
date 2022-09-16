class Solution:
    def partitionString(self, s: str) -> int:
        s1=""
        c=1
        for i in s:
            s1=s1+i
            if(len(set(s1))!=len(s1)):
                s1=""+i
                c+=1
        return c
