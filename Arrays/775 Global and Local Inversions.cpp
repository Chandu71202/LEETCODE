class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) 
    {
        for(int i=0;i<nums.size();i++)
        {
            int x=nums[i]-i;
            if (abs(x)>1)
            {
                return false;
            }
        }
        return true;
    }
};

// Same in Python 226/226 passed but bug with leetcode with TLE
// class Solution:
//     def isIdealPermutation(self, nums: List[int]) -> bool:
//         for i,num in enumerate(nums):
//             if abs(num - i) > 1:
//                 return False
//         return True
