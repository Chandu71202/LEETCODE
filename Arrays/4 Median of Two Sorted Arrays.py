# RUNTIME: 117ms
# optimized one
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        print(nums3)
        if(len(nums3)%2!=0):
            return float(format(nums3[int(len(nums3)/2)],'.5f'))
        else:
            return float(format((nums3[int(len(nums3)/2)]+nums3[int(len(nums3)/2)-1])/2,'.5f'))
#since we added 2 lists it has less time complexity
        
#RUNTIME: 163ms
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for j in nums2:        
            nums1.append(j)
        nums1.sort()
        if(len(nums1)%2!=0):
            temp=len(nums1)-1
            return float((nums1[int(temp/2)]))
        else:
            temp=len(nums1)-1
            return float((nums1[int(temp/2)]+nums1[int(temp/2)+1])/2)
 #since we added nums2 to nums1 using for loop it increased time complexity
