class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        previousRemainder = num
        while num != 1:
            # Factorize as much as we can
            if num % 2 == 0:
                num = num // 2
            if num % 3 == 0:
                num = num // 3
            if num % 5 == 0:
                num = num // 5
            if num == previousRemainder:
                return False
            else:
                previousRemainder = num
        return True
