class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        l = []
        i,j=1,0
        n = len(words)
        while(j<n-1):
            if(sorted(words[i])==sorted(words[i-1])):
                words.pop(i)
                i=i-1
            j+=1
            i+=1
        return words
                
