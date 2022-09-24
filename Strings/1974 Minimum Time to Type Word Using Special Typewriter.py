class Solution:
    def minTimeToType(self, word: str) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = 0
        for i in range(len(word)):
            if i == 0:
                diff = abs(alphabet.index(word[i]) - alphabet.index('a'))
            else:
                diff = abs(alphabet.index(word[i]) - alphabet.index(word[i - 1]))
                
            result += min(diff, 26 - diff)
        return result + len(word)
    
#         ans = (ord('a') - ord(word[0])) % 26
#         ans = min(ans, 26 - ans)
        
#         for i in range(1, len(word)):
#             diff = (ord(word[i]) - ord(word[i-1])) % 26
#             ans += min(diff, 26 - diff)
            
#         return ans + len(word)
