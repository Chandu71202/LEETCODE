class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        max1 = 0
        tokens.sort()
        while tokens:
            if power>=tokens[0]:
                x = tokens.pop(0)
                power-=x
                score += 1
                max1 = max(score,max1)
            elif score > 0:
                x = tokens.pop()
                power+=x
                score-=1 
            else:
                break 
        return max1
