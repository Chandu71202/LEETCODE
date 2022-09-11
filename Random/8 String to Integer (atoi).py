class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if(not s):
            return 0
        val=''
        if(s[0]=='-' or s[0]=='+'):
                val+=s[0] if(s[0]=='-') else ''
                s=s[1:]
        for i in s:
            if(i.isdigit()):
                val+=i
            else:
                break
        if val:
            try:
                if(-(2**31)<=int(val) and int(val) <(2**31)-1):
                    return(int(val))
                else:
                    return -(2**31) if int(val)<0 else 2**31-1
            except:
                return 0
        else:
            return 0
