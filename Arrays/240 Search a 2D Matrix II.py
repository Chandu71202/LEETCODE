class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(row):
            left, right = 0, len(row)
            while(left<=right):
                mid = (right+left)//2
                if row[mid]==target:
                    return True
                elif row[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return False            
            
        for i in matrix:
            if i[0]==target or i[-1]==target:
                return True
            elif i[0]<target and i[-1]>target:
                if search(i):
                    return True 
        return False
