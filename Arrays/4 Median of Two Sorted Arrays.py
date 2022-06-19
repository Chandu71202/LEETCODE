class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        print(nums3)
        if(len(nums3)%2!=0):
            return float(format(nums3[int(len(nums3)/2)],'.5f'))
        else:
            return float(format((nums3[int(len(nums3)/2)]+nums3[int(len(nums3)/2)-1])/2,'.5f'))
