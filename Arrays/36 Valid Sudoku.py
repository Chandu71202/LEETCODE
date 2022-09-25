class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            for j in set(board[i]):
                if j!='.' and board[i].count(j)>1:
                    return False 
        
        for i in range(9):
            l=[board[q][i] for q in range(9)]
            for k in set(l):
                if k!='.' and l.count(k)>1:
                    return False                
                                  
        for i in range(0,9,3):
            for j in range(0,9,3):
                l1 = []
                for p in range(i,i+3):
                    l2 = []
                    for q in range(j,j+3):
                        l2.append(board[p][q])
                    l1.append(l2)
                l = [] 
                for z in l1:
                    l+=z 
                for a in set(l):
                    if a!='.' and l.count(a)>1:
                        return False 
        return True
    
#     for i in range(9):
#             for j in set(board[i]):
#                 if j!='.' and board[i].count(j)>1:
#                     return False
                
#         for i in range(9):
#             l=[board[q][i] for q in range(9)]
#             for j in set(l):
#                 if j!='.' and l.count(j)>1:
#                     return False
                
#         for i in range(0,9,3):
#             for j in range(0,9,3):
#                 l1 = [[board[p][q] for q in range(j,j+3)] for p in range(i,i+3)]
#                 l=[]
#                 for c in l1:
#                     l+=c
#                 for k in set(l):
#                     if k!='.' and l.count(k)>1:
#                         return False
#         return True
                                 
                
