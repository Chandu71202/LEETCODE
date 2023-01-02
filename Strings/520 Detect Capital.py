class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        start = word[0].isupper()
        end = word[-1].isupper()
        n = len(word)
        if start==True and end==True:
            for i in range(1,n):
                if word[i].islower():
                    return False
        elif start==False and end==False:
            for i in range(1,n):
                if word[i].isupper():
                    return False
        else:
            for i in range(1,n):
                if word[i].isupper():
                    return False
        return True
