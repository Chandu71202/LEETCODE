class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(str,s.split()))[::-1])
