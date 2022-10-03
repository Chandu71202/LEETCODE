class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if(r*c!=len(mat)*len(mat[0])):
            return mat
        
        ans= [[]]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                k = mat[i][j]
                if len(ans[-1])<c:
                    ans[-1].append(k)
                else:
                    ans.append([k])
        return ans
