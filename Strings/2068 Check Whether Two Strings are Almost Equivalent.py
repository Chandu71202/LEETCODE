class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        s1 = set(word1)
        s2 = set(word2)
        for i in s1:
            if abs(word1.count(i)-word2.count(i))>=4:
                return False
        for i in s2:
            if abs(word1.count(i)-word2.count(i))>=4:
                return False
        return True
