class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0                      
        j = int(math.sqrt(c)) + 1

        while i <= j:              
            m_sum = i * i + j * j
            if m_sum == c:
                return True
            elif m_sum > c:
                j = j - 1
            else: 
                i = i + 1

        return False
