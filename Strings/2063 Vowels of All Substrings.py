class Solution:
    def countVowels(self, word: str) -> int:
        a = "aeiou"
        c = 0
        n = len(word)
        for i in range(n):
            if word[i] in a:
                c+=(n-i)*(i+1)
        return c
