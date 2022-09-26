class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        return max(map(len, s.split('0'))) > max(map(len, s.split('1')))
