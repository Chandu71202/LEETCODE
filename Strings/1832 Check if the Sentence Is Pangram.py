class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = "qwertyuioplkjhgfdsazxcvbnm"
        return set(a)==set(sentence)
      
#       return len(set(sentence))==26
