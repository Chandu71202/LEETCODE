class Solution:
    def countEven(self, num: int) -> int:
        if num%2:
            return num//2  
        return num//2 - sum(map(int , str(num)))%2
