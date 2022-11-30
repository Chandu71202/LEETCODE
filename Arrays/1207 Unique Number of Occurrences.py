class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        s = set(arr)
        for i in s:
            if arr.count(i) not in d:
                d[arr.count(i)]=i
            else:
                return False
        return True
