class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if( r<0 or c<0 or
                r>=ROWS or c>=COLS or 
                board[r][c]!=word[i]):
                
                return False
            
            char = board[r][c]
            board[r][c]=" "
            
            directions = [ (1, 0), (0, 1), (-1, 0), (0, -1)]
            
            for row_delta, col_delta in directions:
                if dfs(r + row_delta, c + col_delta, i + 1):
                    return True
            
            board[r][c]=char
        
        for i in range(ROWS):
            for j in range(COLS):
                if(word[0]==board[i][j] and dfs(i,j,0)):
                    return True
        
        return False
        
