class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        
        l = 0 
        r  = len(letters)
        
        while l <= r:
            mid = l + (r-l)//2
            
            if letters[mid]> target and letters[mid-1] < target:
                return letters[mid]
            elif letters[mid] > target :
                r = mid - 1
            else:
                l = mid + 1
        return letters[l]
