class Solution:
    # def operation(a):
    #     if "*/+-" not in a:
    #         return a
        
        
    def calculate(self, s: str) -> int:
        def eva(s):
            if('*' not in s and '/' not in s):
                return int(s)
            q=''
            x=[]
            for i in s:
                if(i=='*'):
                    x.append(int(q))
                    x.append(i)
                    q=''
                elif(i=='/'):
                    x.append(int(q))
                    x.append(i)
                    q=''
                else:
                    q+=i
            x.append(int(q))
            i=0
            while(i<len(x)):
                if(x[i]=='*'):
                    x=[x[i-1]*x[i+1]]+x[i+2:]
                    i=0
                if(x[i]=='/'):
                    x=[int(x[i-1]/x[i+1])]+x[i+2:]
                    i=0
                i+=1
            return(x[0])  
        l=[]
        s1=""
        for i in range(len(s)):
            if(s[i]==' '):
                continue
            if(s[i]=='+'):
                l.append(eva(s1))
                s1=""
            elif(s[i]=='-'):
                l.append(eva(s1))
                s1='-'
            else:
                s1=s1+s[i]  

        l.append(eva(s1))
        return sum(l)
                
                
