class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        h=len(s)-1
        while(l<h):
            if(s[l]==s[h]):
                l=l+1
                h=h-1
            else:
                break
        s1 = s[:l] +'' + s[l + 1:]
        s2 = s[:h]+''+s[h+1: ]
        return s1==s1[::-1] or s2==s2[::-1]
