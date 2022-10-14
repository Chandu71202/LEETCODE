class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(row):
            left = 0
            right = len(row)
            while(left<=right):
                mid = left + (right-left)//2
                if row[mid]==target:
                    return True
                if row[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
        
        for i in matrix:
            if target>= i[0] and target<=i[-1]:
                return search(i)
