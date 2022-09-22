class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(map(str,s.split()))
        for i in range(len(l)):
            l[i]=l[i][::-1]
        return ' '.join(l)
