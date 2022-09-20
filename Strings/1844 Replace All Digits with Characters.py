class Solution:
    def replaceDigits(self, s: str) -> str:
        for i in s:
            if i.isnumeric():
                s = s.replace(i, chr(ord(s[s.index(i)-1])+int(i)) ,1)
        return s
