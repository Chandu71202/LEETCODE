class Solution:
     def minimizeXor(self, num1: int, num2: int) -> int:
        n = bin(num2).count('1')
        m = bin(num1).count('1')
        res = num1
        i = 1
        while m > n:
            if res & i:
                res -= i
                m -= 1
            i <<= 1
        while m < n:
            if res & i == 0:
                res += i
                m += 1
            i <<= 1
        return res
