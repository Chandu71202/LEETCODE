class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        res=[]
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            try:
                if i!=d[target-nums[i]]:
                    res.append(i)
                    res.append(d[target-nums[i]])
                    return res
            except:
                res=[]
        return res
      
      
