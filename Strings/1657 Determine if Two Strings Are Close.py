class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def freq(word):
            return sorted(collections.Counter(word).values())
        return freq(word1)==freq(word2) and set(word1)==set(word2)
