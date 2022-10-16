l = set()
temp = 0
class Solution:
    
    def func(self):
        for i in range(50000):
            global l
            l.add(i+int(str(i)[::-1]))
            
    def sumOfNumberAndReverse(self, num: int) -> bool:
        global temp
        if temp ==0:
            self.func()
            temp = 1
        if num in l:
            return True 
        return False 
