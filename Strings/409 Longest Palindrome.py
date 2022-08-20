class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=set()
        for i in s:
            if i not in d:
                d.add(i)
            else:
                d.remove(i)
        if(len(d)!=0):
            return len(s)+1-len(d)
        else:
            return len(s)
