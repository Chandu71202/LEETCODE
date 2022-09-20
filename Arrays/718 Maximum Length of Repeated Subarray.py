class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         s1 = ''.join([chr(x) for x in nums2])
#         s = ""
#         mx = 0
#         for i in nums1:
#             s = s + chr(i)
#             if s in s1:
#                 mx = max(mx,len(s))
#             else:
#                 s = s[1:]
#         return mx
        nums2_str = "".join([chr(x) for x in nums2])
        nums1_str = "".join([chr(x) for x in nums1])
        N = len(nums1_str)
        res = 0
        i = 0
        for j in range(1, N+1):
            if nums1_str[i:j] in nums2_str:
                res = max(res, j-i)
            elif i < j:
                i += 1
        return res

