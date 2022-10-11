import math
class Solution(object): 

    def searchRange(self, nums, target):
        result = [-1, -1]
        result[0] = self.findStartingIndex(nums, target) 
        result[1] = self.findEndingIndex(nums, target)  
        return result

    def findStartingIndex(self, nums, target):
        index = -1 
        low = 0 
        high = len(nums) -1
        
        while low <= high:
            mid = math.floor(low + (high - low)/2)
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1     
        return index
        
  
    def findEndingIndex(self, nums, target):
        index = -1
        low, high = 0, len(nums) -1
        
        while low <= high:
            mid = math.floor(low + (high - low)/2)
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target: 
                high = mid - 1
            else:
                 low = mid + 1
        return index
