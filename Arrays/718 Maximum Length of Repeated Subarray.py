class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = ''.join([chr(x) for x in nums2])
        s = ""
        mx = 0
        for i in nums1:
            s = s + chr(i)
            if s in s1:
                mx = max(mx,len(s))
            else:
                s = s[1:]
        return mx
