class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=0
        for i in words:
            f=0
            for j in i:
                if i.count(j)<=chars.count(j):
                    f=1
                else:
                    f=0
                    break
            if f==1:
                c+=len(i)
        return c
