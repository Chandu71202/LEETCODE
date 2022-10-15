class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for val in arr:
            if d.get(val*2,0) or d.get(val/2,0): return True
            d[val] = 1
        return False
