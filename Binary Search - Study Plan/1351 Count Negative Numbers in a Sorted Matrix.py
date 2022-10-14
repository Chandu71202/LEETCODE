class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bin(row):
            left, right = 0, len(row)
            while left<right:
                mid = left +(right -left) // 2
                if row[mid]<0:
                    right = mid
                else:
                    left = mid+1
            return len(row)- left
        
        count = 0
        for row in grid:
            count += bin(row)
        return(count)
