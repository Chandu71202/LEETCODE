class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator*denominator<0:
            ans="-"
        else:
            ans=""
        q=abs(numerator)//abs(denominator)
        r=abs(numerator)%abs(denominator)
        d=set()
        decimal=[]
        if r==0:
            ans=ans+str(q)
            return ans
        else:
            flag=False
            while r!=0:
                if r not in d:
                    n=r*10
                    q1=n//abs(denominator)
                    d.add(r)
                    decimal.append((q1,r))
                    r=n%abs(denominator)
                else:
                    r1=r
                    flag=True
                    break
        ans+=str(q)+'.'
        if flag==False:
            for Q,R in decimal:
                ans+=str(Q)
        if flag==True:
            for i in range(0,len(decimal)):
                if decimal[i][1]!=r1:
                    ans+=str(decimal[i][0])
                else:
                    break
            ans+='('
            for x in range(i,len(decimal)):
                ans+=str(decimal[x][0])
            ans+=')'        
        return ans
    
    
#         def helper(test_str):
#             res = None
#             temp = (test_str + test_str).find(test_str, 1, -1)
#             if temp != -1:
#                 res = test_str[:temp]
#             if res==None:
#                 return False
#             else:
#                 return res
    
#         if(numerator%denominator==0):
#             a=numerator // denominator
#             return str(a)
#         else:
#             a = str(numerator / denominator)
#             print(numerator / denominator)
#             i = a.find('.')
#             x = a[i+1:]
#             for i in range(len(x)):
#                 h = helper(x[i:])
#                 t = x[:i]
#                 if h!=False:
#                     return str(numerator//denominator)+ '.' + t + "("+h+")"
#             else:
#                 return a
