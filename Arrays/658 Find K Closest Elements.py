class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        
        #find closest element and init two pointers 
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            if (x - arr[mid]) > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left+k]
