class Solution:
    def reverseVowels(self, s: str) -> str:
        ex = 'aeiouAEIOU'
        s = list(s)
        low = 0
        high = len(s)-1
        while(low<high):

            while low<high and s[low] not in ex :
                low+=1
            while low<high and s[high] not in ex :
                high-=1

            s[low],s[high]=s[high],s[low]
            high-=1
            low+=1
            
        return ''.join(s)
