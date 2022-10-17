class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        left, right, ans = 0, 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:
                ans = max(ans, right - left)
                right += 1
            else:
                left += 1
        return ans
