class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%len(nums)
        a = nums[n-k:] + nums[:n-k]
        nums[:] = a
        
        
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = k%len(nums)
#         for i in range(k):
#             nums.insert(0,nums.pop())
