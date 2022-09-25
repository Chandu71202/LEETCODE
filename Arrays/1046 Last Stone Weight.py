class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            stones.sort()
            x = stones[-1]-stones[-2]
            stones.pop()
            stones.pop()
            if x!=0 :
                stones.append(x)
        return stones[0] if stones else 0
