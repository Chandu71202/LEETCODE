class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums)==1:
            if nums[0]!=target:
                return False
            else:
                return True

        left=0
        right=len(nums)-1
        while(left<=right):
            
            while left<right and nums[left]==nums[left+1]:
                left+=1
            while left<right and nums[right]==nums[right-1]:
                right-=1
                
            mid = (left+right)//2
            
            if nums[mid]==target:
                return True
            
            elif nums[left]<=nums[mid]:
                if nums[mid]>=target and nums[left]<=target:
                    right = mid-1
                else:
                    left = mid+1
                    
            else:
                if target>=nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        return False
