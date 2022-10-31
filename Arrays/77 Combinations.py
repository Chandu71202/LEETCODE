class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]
        return map(list,combinations(arr, k))
