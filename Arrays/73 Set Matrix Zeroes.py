class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS=len(matrix),len(matrix[0])
        pos00 = False 
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    
                    if(r>0):
                        matrix[r][0]=0
                    else:
                        pos00=True
        
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0 
                    
        if matrix[0][0]==0:
            for r in range(ROWS):
                matrix[r][0]=0
                
        if pos00:
            for c in range(COLS):
                matrix[0][c]=0
                    
        return matrix
