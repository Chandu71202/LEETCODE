class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        j=0
        for i in mat[:len(mat)//2]:
            s=s+i[0+j]+i[-1-j]
            j=j+1
        for i in mat[len(mat)//2:]:
            s=s+i[0+j]+i[-1-j]
            j=j+1
        if len(mat)&1==0:
            return s
        else:
            return s-mat[len(mat)//2][len(mat)//2]
