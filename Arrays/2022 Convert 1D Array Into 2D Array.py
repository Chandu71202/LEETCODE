class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if(m*n!=len(original)):
            return []
        l = []
        j = 0
        for i in range(m):
            l.append(original[j:j+n])
            j+=n
        return l
