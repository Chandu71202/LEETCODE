class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        for i,val in enumerate(order):
            d[val]=i
        print(d)
        return words==sorted(words,key=lambda x:[d[i]for i in x])
        
