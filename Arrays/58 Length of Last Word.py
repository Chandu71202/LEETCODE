class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(map(str,s.strip().split()))[-1])
        
