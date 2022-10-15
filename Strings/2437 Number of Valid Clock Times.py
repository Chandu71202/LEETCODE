class Solution:
    def countTime(self, findings: str) -> int:
        ans = 1 
        if findings[-1]=='?' and findings[-2]=='?':
            ans = 60
        elif findings[-1]=='?':
            ans = 10
        elif findings[-2]=='?':
            ans = 6
        
        if findings[0]=='?' and findings[1]=='?':
            ans=ans*24
        elif findings[0]=='0'and findings[1]=='?':
            ans = ans*10
        elif findings[0]=='1' and findings[1]=='?':
            ans = ans*10
        elif findings[0]=='2' and findings[1]=='?':
            ans = ans*4
        elif findings[0]=='?' and int(findings[1])<=3:
            ans = ans * 3
        elif findings[0]=='?' and int(findings[1])>=4:
            ans = ans * 2
            
        return ans
            
        
