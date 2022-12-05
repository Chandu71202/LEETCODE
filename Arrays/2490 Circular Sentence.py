class Solution:
    def isCircularSentence(self, sentence: str) -> bool: 
        if sentence[0]!=sentence[-1]:
            return False
        else:
            l = list(map(str,sentence.split(' ')))
            for i in range(1,len(l)):
                if l[i-1][-1]!=l[i][0]:
                    return False
            return True
