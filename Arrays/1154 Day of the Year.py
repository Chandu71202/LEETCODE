class Solution:
    def dayOfYear(self, date: str) -> int:
        # 161 ms
        def leapYear(year):
            if (year % 400 == 0) and (year % 100 == 0):
                return True
            elif (year % 4 == 0) and (year % 100 != 0):
                return True
            else:
                return False
        
        d = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        l=list(map(int,date.split('-')))
        if(leapYear(l[0])):
            d[2]=d[2]+1 
        res=0
        for i in range(1,l[1]):
            res+=d[i]
        res+=l[2]
        return res

# 166 ms
#         month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         year, month, day = map(int, date.split('-'))
        
#         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#             month_days[1] = 29
            
#         res = day
#         for i in range(month - 1):
#             res += month_days[i]
            
#         return res
