class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2)%2:
            for i in nums1:
                ans^=i
        if len(nums1)%2:
            for i in nums2:
                ans^=i
        return ans
