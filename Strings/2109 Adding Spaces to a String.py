class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        spaces = set(spaces)
        for i in range(len(s)):
            if i in spaces:
                result+= ' ' + s[i]
            else:
                result+=s[i]
        return result
