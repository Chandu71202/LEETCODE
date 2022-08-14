class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1=''
        for i in s:
            if(i.isalpha() or i.isnumeric()):
                s1=s1+i
        if(s1==s1[::-1]):
            return 1
        else:
            return 0
