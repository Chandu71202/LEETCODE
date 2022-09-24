class Solution:
    def minTimeToType(self, word: str) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = 0
        for i in range(len(word)):
            if i == 0:
                diff = abs(alphabet.index(word[i]) - alphabet.index('a'))
            else:
                diff = abs(alphabet.index(word[i]) - alphabet.index(word[i - 1]))
                
            result += min(diff, 26 - diff)
        return result + len(word)
